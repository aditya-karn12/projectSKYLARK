# Skylark Drones Business Intelligence Agent

**A founder-facing BI assistant that answers strategic questions on revenue, pipeline health, operational execution, and sector performance.**

The system is designed to work with messy real-world board data, normalizes poor-quality inputs, and returns executive-ready insights instead of raw tables.

**Status**: Production-ready prototype with live Monday.com integration ✅

## 🚀 Quick Deploy (Free)

Deploy to Streamlit Cloud in 2 minutes:
1. Fork this repo to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Add Monday.com API key and board IDs in app settings
5. Share the public URL with your team

👉 See [STREAMLIT_CLOUD_CONFIG.md](STREAMLIT_CLOUD_CONFIG.md) for step-by-step deployment guide.

## Product vision

The prototype solves the problem described in the assignment by combining:

- a modern conversational frontend
- a resilient data-cleaning and analytics layer
- a backend API for BI queries
- a Monday.com-compatible design for future live board integration
- a leadership summary layer for executive updates

## Key product features

- Conversational Q&A for founder-level business questions
- Pipeline analysis across deals and work-order data
- Revenue and collection tracking
- Sector breakdowns and performance insights
- Data-quality guardrails for missing values, blank records, and inconsistent fields
- Executive summary view for board-ready updates
- Monday.com read-only architecture path with environment-based configuration

## Architecture

- `app/streamlit_app.py` — polished Streamlit UI with tabs, charts, and animated glass-panel styling
- `app/api.py` — FastAPI endpoints for query and summary requests
- `app/core/data_loader.py` — workbook ingestion and normalization rules
- `app/core/insights.py` — KPI logic, sector analysis, and business-answer generation
- `app/services/monday_client.py` — placeholder integration client for Monday.com API calls
- `Work_Order_Tracker Data.xlsx` — work-order and execution data
- `Deal funnel Data.xlsx` — sales pipeline data

## Running locally

### Option 1: Streamlit UI only (Recommended for testing)
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```
Open browser at `http://localhost:8501`

### Option 2: Full stack (API + UI) for development
```bash
# Terminal 1: Start backend API
python -m uvicorn app.api:app --host 0.0.0.0 --port 8000

# Terminal 2: Start frontend UI
streamlit run app/streamlit_app.py
```
- API: `http://localhost:8000`
- UI: `http://localhost:8501`

### Option 3: One-command startup
```bash
python main.py
```

## Environment configuration for Monday.com

Create a `.env` file with values like:

```bash
MONDAY_API_KEY=your_api_token
MONDAY_WORK_ORDER_BOARD_ID=5030969735
MONDAY_DEAL_BOARD_ID=5030969736
MONDAY_EXTRA_BOARD_ID_1=5030969738
MONDAY_EXTRA_BOARD_ID_2=5030969733
MONDAY_BASE_URL=https://api.monday.com/v2
```

The app automatically loads `.env` values at startup. It also accepts optional extra board IDs for additional Monday workspace boards. If those boards do not match the expected Work Orders / Deals schema, the app falls back to the local Excel files without failing the experience.

## Deployment (Hosted Prototype)

### Deploy to Streamlit Cloud (Free & Easy)
See [STREAMLIT_CLOUD_CONFIG.md](STREAMLIT_CLOUD_CONFIG.md) for complete instructions.

### Deploy to Heroku
See [DEPLOYMENT.md](DEPLOYMENT.md) for Heroku and other platform options.

## Resilience approach

The solution handles real-world dirty data by:

- replacing missing numbers with zero when safe
- using `Unknown` for blank categorical values
- normalizing common sector and status labels
- flagging data-quality issues in a dedicated dashboard area
- avoiding failure when records are incomplete

## Decision log

The design assumptions and trade-offs are documented in [decision_log.md](decision_log.md).

## Extensibility

The strongest next iteration would add:

- an LLM-based query planner
- richer PDF/board exports for leadership decks
- live Monday.com schema mapping and board-to-analytics synchronization
