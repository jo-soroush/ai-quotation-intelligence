"""AWS Lambda entrypoint for the delivered C13 application.

Constructing this module performs no AWS call. The C08 provider creates its
client only when an analysis/draft request actually invokes the model.
"""

from mangum import Mangum

from ai_quotation_intelligence.agent_tools import AgentTools
from ai_quotation_intelligence.api import create_app
from ai_quotation_intelligence.bedrock import BedrockConverseAdapter
from ai_quotation_intelligence.config import load_settings
from ai_quotation_intelligence.quotation_agent import QuotationAgent


app = create_app(QuotationAgent(BedrockConverseAdapter(load_settings()), AgentTools()))
_adapter = Mangum(app, lifespan="off")


def handler(event: object, context: object) -> dict[str, object]:
    """Adapt a proxy event, containing unexpected adapter errors at the edge."""

    try:
        return _adapter(event, context)
    except Exception:
        return {
            "statusCode": 500,
            "headers": {"content-type": "application/json"},
            "body": '{"code":"internal_error"}',
            "isBase64Encoded": False,
        }
