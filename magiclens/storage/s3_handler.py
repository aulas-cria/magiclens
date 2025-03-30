import boto3
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

    def save_image(self, filename: str, content: str):
        self.__put_object(filename=filename, content=content)

    def __create_bucket(self):
        self.s3.create_bucket(Bucket=self.bucket_name)

    def __put_object(self, filename: str, content: str):
        self.s3.put_object(
            Bucket=self.bucket_name, Key=filename, Body=content
        )

    def __get_object(self, key: str):
        return self.s3.get_object(
            Bucket=self.bucket_name, Key=key
        )