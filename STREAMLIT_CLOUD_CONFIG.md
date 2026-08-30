# Streamlit Cloud Configuration for Skylark Drones BI Agent

## Files in this directory

- `app.py` - Production Streamlit application (main entry point)
- `requirements.txt` - Python package dependencies
- `streamlit_config.toml` - Streamlit UI configuration
- `secrets.toml` - Local development secrets (add to .gitignore)
- `Procfile` - Heroku deployment configuration
- `vercel.json` - Vercel deployment configuration (optional)
- `DEPLOYMENT.md` - Detailed deployment guide
- `app/` - Core application package with:
  - `api.py` - FastAPI backend
  - `streamlit_app.py` - Local development UI
  - `config.py` - Configuration management
  - `core/` - Business logic (data_loader, insights)
  - `services/` - Monday.com API client

## Deployment Instructions

### Streamlit Cloud (Recommended - Simplest)

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Skylark Drones BI Agent"
   git push origin main
   ```

2. **Deploy to Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your GitHub repo
   - Choose branch and file: `app.py`

3. **Add Secrets**
   - In app settings, go to Secrets
   - Add your Monday.com API key and board IDs

4. **Live URL**
   - Your app will be available at a public URL
   - Share with team/stakeholders

### Heroku Deployment

1. **Install Heroku CLI**
   ```bash
   brew install heroku  # macOS
   # or download from heroku.com/download
   ```

2. **Login and create app**
   ```bash
   heroku login
   heroku create skylark-drones-bi
   ```

3. **Set environment variables**
   ```bash
   heroku config:set MONDAY_API_KEY="your_key"
   heroku config:set MONDAY_WORK_ORDER_BOARD_ID="5030969735"
   heroku config:set MONDAY_DEAL_BOARD_ID="5030969736"
   ```

4. **Deploy**
   ```bash
   git push heroku main
   heroku open
   ```

### Railway.app Deployment

1. Go to [railway.app](https://railway.app)
2. Click "Create New Project"
3. Connect GitHub repo
4. Add environment variables
5. Deploy automatically

## Environment Variables Required

```
MONDAY_API_KEY=your_api_token
MONDAY_WORK_ORDER_BOARD_ID=5030969735
MONDAY_DEAL_BOARD_ID=5030969736
MONDAY_EXTRA_BOARD_ID_1=5030969738
MONDAY_EXTRA_BOARD_ID_2=5030969733
MONDAY_BASE_URL=https://api.monday.com/v2
```

## Testing Deployed App

Once deployed:
1. View executive dashboard with live KPIs
2. Ask business questions
3. Generate executive summaries
4. Check system status

## Support

For deployment issues:
- Check `DEPLOYMENT.md` for troubleshooting
- Verify `requirements.txt` is up to date
- Ensure environment variables are set correctly
- Check platform logs for error messages

## Tech Stack

- **Frontend**: Streamlit (Python)
- **Backend**: FastAPI (Python)
- **Data**: Pandas, SQLite (optional)
- **Visualization**: Plotly
- **Integration**: Monday.com GraphQL API
- **Deployment**: Streamlit Cloud / Heroku / Railway

## Production Notes

- Never commit `.env` or secrets to version control
- Use platform-specific secret management
- Cold start time may be 30-60 seconds on free tiers
- All data is read-only from Monday.com
- No data modifications or writes are performed
