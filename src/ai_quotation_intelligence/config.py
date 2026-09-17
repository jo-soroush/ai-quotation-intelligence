"""Environment-backed application configuration boundary."""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    """Non-secret baseline settings loaded from environment variables."""

    app_name: str = "AI Quotation Intelligence"
    environment: str = "local"
    log_level: str = "INFO"
    aws_region: str = "us-east-1"
    bedrock_model_id: str = "amazon.nova-micro-v1:0"
    bedrock_max_tokens: int = 64
    bedrock_temperature: float = 0.0
    bedrock_connect_timeout: int = 5
    bedrock_read_timeout: int = 30
    bedrock_max_attempts: int = 2


def load_settings() -> Settings:
    """Load baseline settings without reading or containing credentials."""

    return Settings(
        app_name=os.getenv("AQI_APP_NAME", Settings.app_name),
        environment=os.getenv("AQI_ENVIRONMENT", Settings.environment),
        log_level=os.getenv("AQI_LOG_LEVEL", Settings.log_level),
        aws_region=os.getenv("AQI_AWS_REGION", Settings.aws_region),
        bedrock_model_id=os.getenv("AQI_BEDROCK_MODEL_ID", Settings.bedrock_model_id),
        bedrock_max_tokens=int(os.getenv("AQI_BEDROCK_MAX_TOKENS", str(Settings.bedrock_max_tokens))),
        bedrock_temperature=float(os.getenv("AQI_BEDROCK_TEMPERATURE", str(Settings.bedrock_temperature))),
        bedrock_connect_timeout=int(os.getenv("AQI_BEDROCK_CONNECT_TIMEOUT", str(Settings.bedrock_connect_timeout))),
        bedrock_read_timeout=int(os.getenv("AQI_BEDROCK_READ_TIMEOUT", str(Settings.bedrock_read_timeout))),
        bedrock_max_attempts=int(os.getenv("AQI_BEDROCK_MAX_ATTEMPTS", str(Settings.bedrock_max_attempts))),
    )
