"""
Production-ready Streamlit app for Skylark Drones BI Agent
Optimized for Streamlit Cloud deployment
"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from secrets or .env
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Add app to path
sys.path.insert(0, str(BASE_DIR))

from app import get_insight_engine, get_source_status


st.set_page_config(
    page_title="Skylark Drones BI Agent",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown("""
<style>
    [data-testid="stMainBlockContainer"] {
        padding-top: 1rem;
    }
    .kpi-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        padding: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .metric-value {
        font-size: 28px;
        font-weight: bold;
        margin: 10px 0;
    }
    .metric-label {
        font-size: 14px;
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "engine" not in st.session_state:
    try:
        st.session_state.engine = get_insight_engine()
    except Exception as e:
        st.error(f"Failed to initialize analytics engine: {str(e)}")
        st.stop()

if "source_status" not in st.session_state:
    st.session_state.source_status = get_source_status()

# Header
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("# 🚀 Skylark Drones - Business Intelligence Agent")
    st.markdown("*Founder-level insights on pipeline, revenue, and operational execution*")

with col2:
    source = st.session_state.source_status["source"]
    if source == "monday.com":
        st.success(f"📊 Live {source.upper()} ✅")
    else:
        st.info(f"📁 {source.upper()} ℹ️")

st.divider()

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Executive Dashboard",
    "💬 Ask Questions",
    "📋 Executive Summary",
    "⚙️ System Status"
])

# ===================== TAB 1: DASHBOARD =====================
with tab1:
    try:
        kpis = st.session_state.engine.get_kpis()
        
        # KPI Row 1
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Total Pipeline",
                f"₹{kpis['total_pipeline']/1e7:.2f}Cr",
                f"Open: ₹{kpis['open_pipeline']/1e7:.2f}Cr"
            )
        
        with col2:
            st.metric(
                "Total Revenue",
                f"₹{kpis['total_revenue']/1e7:.2f}Cr",
                f"Collected: {kpis['collection_rate_percent']:.1f}%"
            )
        
        with col3:
            st.metric(
                "Collection Amount",
                f"₹{kpis['collected_amount']/1e7:.2f}Cr",
                f"Billed: ₹{kpis['billed_amount']/1e7:.2f}Cr"
            )
        
        with col4:
            st.metric(
                "Deal Health",
                f"{kpis['open_deal_count']} Open",
                f"Closed: {kpis['dead_deal_count']}"
            )
        
        st.divider()
        
        # Charts
        col1, col2 = st.columns(2)
        
        with col1:
            sector_breakdown = st.session_state.engine.get_sector_breakdown()
            if sector_breakdown and "sector_revenue" in sector_breakdown:
                fig = px.bar(
                    x=list(sector_breakdown["sector_revenue"].keys()),
                    y=list(sector_breakdown["sector_revenue"].values()),
                    title="Revenue by Sector",
                    labels={"x": "Sector", "y": "Revenue (₹)"},
                    color=list(sector_breakdown["sector_revenue"].values()),
                    color_continuous_scale="Viridis"
                )
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            sector_breakdown = st.session_state.engine.get_sector_breakdown()
            if sector_breakdown and "sector_pipeline" in sector_breakdown:
                fig = px.pie(
                    values=list(sector_breakdown["sector_pipeline"].values()),
                    names=list(sector_breakdown["sector_pipeline"].keys()),
                    title="Pipeline Distribution by Sector"
                )
                st.plotly_chart(fig, use_container_width=True)
        
        st.info(f"📊 Data Quality: {kpis.get('quality_note', 'Data normalized and ready for analysis')}")
        
    except Exception as e:
        st.error(f"Error loading dashboard: {str(e)}")

# ===================== TAB 2: QUESTIONS =====================
with tab2:
    st.markdown("## Ask Business Questions")
    st.markdown("*Examples: How's our pipeline by sector? What's our collection rate? Revenue trends?*")
    
    question = st.text_area(
        "What do you want to know about the business?",
        placeholder="e.g., How much revenue did we collect this quarter?",
        height=80
    )
    
    col1, col2 = st.columns([3, 1])
    with col2:
        ask_button = st.button("Ask", key="ask_btn", use_container_width=True)
    
    if ask_button and question:
        try:
            with st.spinner("Analyzing data..."):
                answer = st.session_state.engine.answer_query(question)
                
            st.markdown("### Answer")
            st.write(answer.get("answer", "No answer generated"))
            
            if answer.get("caveat"):
                st.warning(f"📌 Data Note: {answer['caveat']}")
        
        except Exception as e:
            st.error(f"Error processing query: {str(e)}")

# ===================== TAB 3: EXECUTIVE SUMMARY =====================
with tab3:
    try:
        summary = st.session_state.engine.get_leadership_summary()
        
        st.markdown("## Leadership Briefing")
        st.markdown(summary.get("summary", "Summary not available"))
        
        # Key insights section
        if summary.get("key_insights"):
            st.markdown("### Key Insights")
            for insight in summary.get("key_insights", []):
                st.markdown(f"- {insight}")
        
        # Recommendations
        if summary.get("recommendations"):
            st.markdown("### Recommendations")
            for rec in summary.get("recommendations", []):
                st.markdown(f"- {rec}")
        
        st.markdown(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
        
    except Exception as e:
        st.error(f"Error generating summary: {str(e)}")

# ===================== TAB 4: SYSTEM STATUS =====================
with tab4:
    st.markdown("## System Configuration")
    
    status = st.session_state.source_status
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Data Source")
        st.json({
            "source": status["source"],
            "monday_connected": status["monday_connected"],
            "board_ids_configured": status["board_ids_configured"],
            "local_fallback_active": status["local_fallback_active"]
        })
    
    with col2:
        st.markdown("### Requirements Status")
        reqs = status.get("requirements_status", {})
        for req, met in reqs.items():
            status_icon = "✅" if met else "❌"
            st.write(f"{status_icon} {req.replace('_', ' ').title()}")
    
    st.divider()
    st.markdown("### About")
    st.markdown("""
    **Skylark Drones Business Intelligence Agent**
    
    A founder-facing BI assistant that answers strategic questions across your business data.
    The system integrates with monday.com boards and provides:
    
    - Conversational Q&A for business insights
    - Executive summaries for leadership updates
    - KPI dashboards and sector analysis
    - Resilient data handling for messy real-world data
    
    **Assignment**: Skylark Drones - Full Stack BI Agent  
    **Stack**: Streamlit + FastAPI + Monday.com API + Pandas  
    **Status**: Production Ready ✅
    """)
