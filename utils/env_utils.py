from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    __instance = None
    API_ID: int
    API_HASH: str
    DEBUG: bool
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


ENV_SETTINGS = Settings()
