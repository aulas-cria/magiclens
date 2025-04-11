import os

from magiclens.storage.storage_handler import StorageHandler

class LocalHandler(StorageHandler):
    def __init__(self, base_path: str):
        self.base_path = base_path

    def save(self, filename: str, content: any) -> str:
        file_path = os.path.join(self.base_path, filename)
        
        with open(file_path, 'wb') as f:
            f.write(content)

        return f'{self.base_path}/{filename}'

    def get(self, filename: str) -> str:
        file_path = os.path.join(self.base_path, filename)
        return file_path
