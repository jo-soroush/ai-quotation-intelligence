from ai_quotation_intelligence import __version__
from ai_quotation_intelligence.config import Settings, load_settings
from ai_quotation_intelligence.logging_config import configure_logging


def test_package_imports() -> None:
    assert __version__ == "0.1.0"


def test_configuration_loads_from_environment(monkeypatch) -> None:
    monkeypatch.setenv("AQI_ENVIRONMENT", "test")
    settings = load_settings()

    assert isinstance(settings, Settings)
    assert settings.environment == "test"
    assert settings.app_name == "AI Quotation Intelligence"


def test_logging_boundary_returns_package_logger() -> None:
    logger = configure_logging()

    assert logger.name == "ai_quotation_intelligence"
