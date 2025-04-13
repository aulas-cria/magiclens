class StorageHandler:
    def save(self, filename: str, content: bytes) -> str:
        pass

    def get_path(self, filename: str, base_path_system: bool = False) -> str:
        pass

    def get(self, filename: str)-> bytes | None:
        pass