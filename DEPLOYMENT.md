# Streamlit Cloud Deployment Guide

## Quick Deploy to Streamlit Cloud (Free)

### Step 1: Prepare your GitHub repository
1. Fork or create a GitHub repo with the project files
2. Ensure `.env` is in `.gitignore` (never commit secrets)

### Step 2: Deploy to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Select your GitHub repo
4. Choose the branch and file: `app.py`

### Step 3: Add Secrets
1. In Streamlit Cloud dashboard, click your app
2. Go to Settings → Secrets
3. Add your Monday.com credentials:

```
MONDAY_API_KEY=your_api_token
MONDAY_WORK_ORDER_BOARD_ID=5030969735
MONDAY_DEAL_BOARD_ID=5030969736
MONDAY_EXTRA_BOARD_ID_1=5030969738
MONDAY_EXTRA_BOARD_ID_2=5030969733
MONDAY_BASE_URL=https://api.monday.com/v2
```

### Step 4: Your app is live!
Your unique URL will be: `https://[username]-[appname].streamlit.app`

---

## Alternative: Deploy to Heroku

### Prerequisites
- Heroku CLI installed
- Heroku account (free tier available)

### Steps
1. Login to Heroku:
```bash
heroku login
```

2. Create a new app:
```bash
heroku create skylark-drones-bi
```

3. Add secrets:
```bash
heroku config:set MONDAY_API_KEY="your_token"
heroku config:set MONDAY_WORK_ORDER_BOARD_ID="5030969735"
heroku config:set MONDAY_DEAL_BOARD_ID="5030969736"
```

4. Deploy:
```bash
git push heroku main
```

Your app will be at: `https://skylark-drones-bi.herokuapp.com`

---

## Alternative: Deploy to Railway

1. Go to [railway.app](https://railway.app)
2. Click "Create New Project"
3. Connect your GitHub repo
4. Add environment variables
5. Deploy

---

## Testing the Hosted Prototype

Once deployed, you can:
1. View live KPI metrics
2. Ask business questions in natural language
3. Generate executive summaries
4. Access system status and configuration

No local setup required - just share the public URL!

---

## Troubleshooting

**"API Token not configured"**
- Ensure MONDAY_API_KEY is added to platform secrets (not .env file)

**"Board IDs not found"**
- Verify board IDs are correct
- Check that your API token has read access to those boards

**"Connection timeout"**
- Free tier platforms may have slower cold starts
- First load can take 30-60 seconds

---

## Files Required for Deployment

- `app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies
- `streamlit_config.toml` - Streamlit configuration
- `app/` - Core application package
- `.streamlit/secrets.toml` - Local secrets (NOT committed)

Never commit `.env` or actual secrets to GitHub!
