import os

from magiclens.storage.storage_handler import StorageHandler
from magiclens.config import Settings

class LocalHandler(StorageHandler):
    def __init__(self):
        self.base_path_system = os.path.join(
            'magiclens',
            'static',
            Settings().bucket_name
        )
        self.base_path_app = Settings().bucket_name

    def save(self, filename: str, content: bytes, base_path_system: bool = False):
        filename_system = os.path.join(self.base_path_system, filename)

        file_path_system = os.path.dirname(filename_system)

        os.makedirs(file_path_system, exist_ok=True)

        with open(filename_system, 'wb') as f:
            f.write(content)

        if base_path_system:
            return os.path.join(self.base_path_system, filename)

        return os.path.join(self.base_path_app, filename)

    def get_path(self, filename: str, base_path_system: bool = False):
        filename_system = os.path.join(self.base_path_system, filename)
        
        if not os.path.exists(filename_system):
            return None

        if base_path_system:
            return os.path.join(self.base_path_system, filename)
        
        return os.path.join(self.base_path_app, filename)

    def get(self, filename: str):
        filename_system = self.get_path(
            filename=filename,
            base_path_system=True
        )

        if filename_system is None:
            return None
        
        with open(filename_system, 'rb') as f:
            return f.read()