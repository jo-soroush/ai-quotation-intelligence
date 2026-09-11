"""Environment-backed application configuration boundary."""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    """Non-secret baseline settings loaded from environment variables."""

    app_name: str = "AI Quotation Intelligence"
    environment: str = "local"
    log_level: str = "INFO"


def load_settings() -> Settings:
    """Load baseline settings without reading or containing credentials."""

    return Settings(
        app_name=os.getenv("AQI_APP_NAME", Settings.app_name),
        environment=os.getenv("AQI_ENVIRONMENT", Settings.environment),
        log_level=os.getenv("AQI_LOG_LEVEL", Settings.log_level),
    )
