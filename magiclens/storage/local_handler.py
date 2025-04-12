import os

from magiclens.storage.storage_handler import StorageHandler

class LocalHandler(StorageHandler):
    def __init__(self, base_path: str):
        self.base_path = base_path

    def save(self, filename: str, content: any) -> str:
        filename_parts = filename.split('/')

        file_path = os.path.join(
            self.base_path,
            *filename_parts[:-1]
        )
        filename = filename_parts[-1]

        os.makedirs(file_path, exist_ok=True)

        with open(os.path.join(file_path, filename), 'wb') as f:
            f.write(content)

        return f'{self.base_path}/{filename}'

    def get(self, filename: str) -> str:
        file_path = os.path.join(self.base_path, filename)
        
        if not os.path.exists(file_path):
            return None
        
        with open(file_path, 'rb') as f:
            return f.read()
