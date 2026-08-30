from pathlib import Path
import os

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

WORK_ORDERS_PATH = BASE_DIR / "Work_Order_Tracker Data.xlsx"
DEALS_PATH = BASE_DIR / "Deal funnel Data.xlsx"

MONDAY_API_KEY = os.getenv("MONDAY_API_KEY")
MONDAY_WORK_ORDER_BOARD_ID = os.getenv("MONDAY_WORK_ORDER_BOARD_ID")
MONDAY_DEAL_BOARD_ID = os.getenv("MONDAY_DEAL_BOARD_ID")
MONDAY_EXTRA_BOARD_ID_1 = os.getenv("MONDAY_EXTRA_BOARD_ID_1")
MONDAY_EXTRA_BOARD_ID_2 = os.getenv("MONDAY_EXTRA_BOARD_ID_2")
MONDAY_BASE_URL = os.getenv("MONDAY_BASE_URL", "https://api.monday.com/v2")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
