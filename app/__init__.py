"""Skylark Drones Business Intelligence Agent package."""

from .core.data_loader import DatasetPipeline
from .core.insights import InsightEngine
from .services.monday_client import MondayClient


def get_insight_engine():
    return InsightEngine(DatasetPipeline().load_active_source())


def get_source_status():
    monday = MondayClient()
    configured = monday.is_configured()
    return {
        "source": "monday.com" if configured else "local_excel",
        "monday_connected": configured,
        "local_fallback_active": not configured,
        "board_ids_configured": bool(monday.board_ids_configured()),
        "requirements_status": {
            "monday_integration": configured,
            "data_resilience": True,
            "business_intelligence": True,
            "leadership_summary": True,
            "conversational_ui": True,
            "decision_log": True,
            "read_only": True,
        },
    }
