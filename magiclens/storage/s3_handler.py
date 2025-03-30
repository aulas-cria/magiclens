import boto3

from botocore.exceptions import ClientError

from magiclens.storage.storage_handler import StorageHandler
from magiclens.config import Settings

class S3Handler(StorageHandler):
    def __init__(self):
        self.s3 = boto3.client(
            "s3",
            endpoint_url=Settings().endpoint_url,
            aws_access_key_id=Settings().access_key,
            aws_secret_access_key=Settings().secret_key,
        )
        self.bucket_name = Settings().bucket_name

    def save(self, filename: str, content: str):
        return self.s3.upload_file(
            Filename=filename.split('/')[-1],
            Bucket=self.bucket_name,
            Key=filename,
            Body=content,
            ContentType=content.content_type,
            Metadata={
                "filename": filename,
                "content-type": content.content_type,
            }
        )

    def get(self, filename: str):
        try:
            return self.__get_object(filename=filename)
        except Exception as e:
            return

    def __create_bucket(self):
        self.s3.create_bucket(Bucket=self.bucket_name)

    def __get_object(self, filename: str):
        return self.s3.get_object(
            Bucket=self.bucket_name, Key=filename
        )