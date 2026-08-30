# 🚀 Quick Start Guide - Skylark Drones BI Agent

## What is this?

A production-ready AI Business Intelligence Agent that answers founder-level questions about your business data (pipeline, revenue, execution) using live Monday.com board integration.

## Current Status

✅ **FULLY OPERATIONAL**
- Live Monday.com integration: **ACTIVE**
- API Token: **CONFIGURED**
- Work Orders Board: **CONNECTED** (5030969735)
- Deals Board: **CONNECTED** (5030969736)
- Backend API: **RUNNING** (http://localhost:8000)
- Streamlit UI: **RUNNING** (http://localhost:8501)

## What You Have

### 1. **Local Development Environment**
- Running at `http://localhost:8501`
- Connected to your live Monday.com boards
- Ready to test immediately

### 2. **Deployment-Ready Code**
- Production Streamlit app (`app.py`)
- Deployment configurations for multiple platforms
- Full documentation and guides

### 3. **Complete Documentation**
- README.md - Overview and setup
- decision_log.md - Design decisions
- DEPLOYMENT.md - Deploy to cloud
- STREAMLIT_CLOUD_CONFIG.md - Streamlit Cloud specific
- DEPLOYMENT_CHECKLIST.md - Verification checklist

## Quick Actions

### Test Locally (Right Now)
Your app is already running at: **http://localhost:8501**

1. Open the browser link
2. Try the examples:
   - "What's our total pipeline value?"
   - "Show me revenue by sector"
   - "How's our collection rate?"

### Deploy to Cloud (2 Minutes)

#### Option A: Streamlit Cloud (Free, Recommended)
```
1. Push your code to GitHub
2. Go to share.streamlit.io
3. Select your GitHub repo
4. Add your Monday.com API key in Secrets
5. Done! Share the public link
```
👉 Full guide: [STREAMLIT_CLOUD_CONFIG.md](STREAMLIT_CLOUD_CONFIG.md)

#### Option B: Heroku
```
heroku login
heroku create skylark-drones-bi
heroku config:set MONDAY_API_KEY="your_token"
git push heroku main
```
👉 Full guide: [DEPLOYMENT.md](DEPLOYMENT.md)

## Key Features

✓ **Conversational Interface**
- Ask questions in natural language
- Get executive-ready answers

✓ **Live Data Integration**
- Real-time Monday.com board data
- Automatic data cleaning and normalization

✓ **Executive Dashboards**
- KPI cards (pipeline, revenue, collection rate)
- Sector analysis charts
- Deal health metrics

✓ **Leadership Summaries**
- Auto-generated briefing for board updates
- Key insights and recommendations
- Sector performance breakdown

✓ **Data Resilience**
- Handles messy real-world data
- Reports data quality issues
- Never crashes on bad data

## Directory Structure

```
projectSKY/
├── app.py                           # Main Streamlit app (production)
├── main.py                          # Local development runner
├── requirements.txt                 # Python dependencies
├── .env                            # Your config (API token, board IDs)
├── .gitignore                      # Prevents secrets from git
├── README.md                       # Main documentation
├── decision_log.md                 # Design decisions
├── DEPLOYMENT.md                   # Cloud deployment guide
├── STREAMLIT_CLOUD_CONFIG.md       # Streamlit Cloud specific
├── DEPLOYMENT_CHECKLIST.md         # Verification checklist
├── Procfile                        # Heroku config
├── streamlit_config.toml           # UI configuration
│
├── app/
│   ├── __init__.py
│   ├── api.py                      # FastAPI backend
│   ├── streamlit_app.py            # Local dev UI
│   ├── config.py                   # Settings
│   ├── core/
│   │   ├── data_loader.py          # Data ingestion
│   │   └── insights.py             # BI logic
│   └── services/
│       └── monday_client.py        # Monday.com API
│
└── Data Files/
    ├── Work_Order_Tracker Data.xlsx
    └── Deal funnel Data.xlsx
```

## Environment Variables

Your `.env` file is already configured:

```env
MONDAY_API_KEY=your_token
MONDAY_WORK_ORDER_BOARD_ID=5030969735
MONDAY_DEAL_BOARD_ID=5030969736
MONDAY_EXTRA_BOARD_ID_1=5030969738
MONDAY_EXTRA_BOARD_ID_2=5030969733
```

## FAQ

**Q: Can I deploy without Monday.com setup?**
A: Yes! The app has Excel fallback. But you have live Monday.com configured already.

**Q: Is my API token secure?**
A: Yes. It's in `.env` which is gitignored and never committed to GitHub.

**Q: How much does it cost to deploy?**
A: Free! Streamlit Cloud and Heroku free tier both work great.

**Q: Can multiple people use it?**
A: Yes! Deployed on cloud, anyone with the URL can use it.

**Q: Can I modify queries/analytics?**
A: Yes! Edit `app/core/insights.py` to customize business logic.

## Next Steps

1. **[If testing locally]** Open http://localhost:8501 and explore
2. **[If deploying]** Follow [STREAMLIT_CLOUD_CONFIG.md](STREAMLIT_CLOUD_CONFIG.md)
3. **[If customizing]** Edit `app/core/insights.py` for your metrics
4. **[Questions?]** Check README.md or DEPLOYMENT.md

## Support

- **Setup Issues**: See [DEPLOYMENT.md](DEPLOYMENT.md) troubleshooting
- **Code Changes**: See [decision_log.md](decision_log.md) for architecture notes
- **Deployment Help**: See [STREAMLIT_CLOUD_CONFIG.md](STREAMLIT_CLOUD_CONFIG.md)

---

## TL;DR

**What**: AI business intelligence agent for Monday.com
**Status**: Live and working right now (http://localhost:8501)
**Deploy**: 2 minutes to cloud (Streamlit/Heroku/Railway)
**Cost**: Free
**Next**: Pick a deployment option and deploy!

👉 **Start here**: [STREAMLIT_CLOUD_CONFIG.md](STREAMLIT_CLOUD_CONFIG.md)
