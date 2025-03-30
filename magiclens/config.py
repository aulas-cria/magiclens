from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    access_key: str
    secret_key: str
    bucket_name: str = 'imagens'
    endpoint_url: str = 'http://localhost:9000'

    model_config = SettingsConfigDict(env_file=".env")
