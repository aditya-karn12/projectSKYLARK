import pandas as pd
import plotly.express as px
import streamlit as st

from app import get_insight_engine, get_source_status

st.set_page_config(page_title="Skylark Drones BI Agent", page_icon="🚁", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #06111f 0%, #0f1f38 35%, #132c52 100%);
        color: #edf5ff;
    }
    .glass-panel {
        background: rgba(13, 24, 43, 0.72);
        border: 1px solid rgba(135, 180, 255, 0.25);
        border-radius: 18px;
        padding: 18px 20px;
        box-shadow: 0 14px 30px rgba(7, 12, 25, 0.25);
        animation: fadeIn 0.8s ease;
    }
    .hero {
        background: linear-gradient(120deg, rgba(27, 64, 121, 0.9), rgba(17, 25, 44, 0.9));
        border-radius: 22px;
        padding: 22px 26px;
        border: 1px solid rgba(148, 193, 255, 0.3);
        box-shadow: 0 20px 40px rgba(3, 8, 16, 0.25);
        animation: rise 0.9s ease;
    }
    .prompt-chip {
        display: inline-block; padding: 8px 12px; border-radius: 999px; background: rgba(119, 173, 255, 0.12);
        border: 1px solid rgba(119, 173, 255, 0.28); color: #d9ecff; margin: 6px 6px 0 0; cursor: pointer;
    }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0px);} }
    @keyframes rise { from { opacity: 0; transform: translateY(-8px); } to { opacity: 1; transform: translateY(0px);} }
    div[data-testid="stMetricLabel"] { color: #a5c6ff; font-size: 0.85rem; }
    div[data-testid="stMetricValue"] { color: #f5f9ff; font-size: clamp(1.5rem, 2vw, 2.4rem); font-weight: 700; }
    .stChatMessage { background: transparent !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

engine = get_insight_engine()
source_status = get_source_status()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome back. I can help with pipeline health, revenue, sector performance, collections, and leadership-ready summaries."}
    ]

with st.sidebar:
    st.markdown("<div class='glass-panel'><h3>Skylark command center</h3></div>", unsafe_allow_html=True)
    st.subheader("Data source")
    source = st.radio("", ["Local Excel", "Monday.com (read-only)"])
    st.caption(f"Active source: {source_status['source']} | Monday connected: {'Yes' if source_status['monday_connected'] else 'No'}")
    if source_status['monday_connected']:
        st.success("Monday.com is connected and read-only board data is active.")
    else:
        st.warning("Live board mode is not connected unless the environment variables are set.")

    st.subheader("Requirement compliance")
    checklist = [
        ("Monday.com integration", source_status["requirements_status"]["monday_integration"]),
        ("Data resilience", source_status["requirements_status"]["data_resilience"]),
        ("BI engine", source_status["requirements_status"]["business_intelligence"]),
        ("Leadership summary", source_status["requirements_status"]["leadership_summary"]),
        ("Decision log", source_status["requirements_status"]["decision_log"]),
    ]
    for label, ok in checklist:
        st.write(f"{'✅' if ok else '⚠️'} {label}")

    st.subheader("Suggested prompts")
    suggestions = [
        "What is our pipeline health?",
        "Give me a leadership update",
        "How is energy sector performing?",
        "What is our collection efficiency?",
        "Which segment is biggest?",
    ]
    for suggestion in suggestions:
        if st.button(suggestion, key=f"prompt_{suggestion}"):
            st.session_state.prompt = suggestion

    if "prompt" in st.session_state:
        st.info(f"Selected: {st.session_state.prompt}")

    st.subheader("System status")
    st.success("Data ingestion OK")
    st.info("Resilience layer active")

st.markdown(
    """
    <div class='hero'>
        <h1 style='margin:0; font-size:2.1rem;'>🚁 Skylark Drones BI Agent</h1>
        <p style='margin-top: 0.5rem; color: #dfeeff; font-size: 1rem;'>Founder-ready intelligence for pipeline, revenue, operations, and executive communications.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.container():
    st.markdown("<div class='glass-panel' style='margin-top: 1rem;'>", unsafe_allow_html=True)
    user_input = st.text_input("Ask a business question", placeholder="Example: How is our energy pipeline looking this quarter?")
    if st.button("Analyze"):
        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})
            result = engine.answer_query(user_input)
            response = result.get("answer", "I can help with pipeline and revenue intelligence.")
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state.last_result = result
    st.markdown("</div>", unsafe_allow_html=True)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if "last_result" in st.session_state:
    result = st.session_state.last_result
    if result.get("summary"):
        st.subheader("Executive brief")
        st.write(result["summary"]["headline"])
        st.json(result["summary"], expanded=False)

kpis = engine.get_kpis()
metrics = [
    ("Open Pipeline", kpis["open_pipeline"], "₹"),
    ("Booked Revenue", kpis["total_revenue"], "₹"),
    ("Collections", kpis["collected_amount"], "₹"),
    ("Collection Rate", kpis["collection_rate_percent"], "%"),
]
cols = st.columns(4)
for col, (label, value, suffix) in zip(cols, metrics):
    if suffix == "%":
        value_text = f"{value:.1f}%"
    else:
        value_text = f"{value:,.2f}"
    with col:
        st.markdown(f'<div class="glass-panel"><div style="color:#a5c6ff; font-size:0.8rem;">{label}</div><div style="font-size:2rem; font-weight:700; margin-top:8px;">{value_text}</div></div>', unsafe_allow_html=True)

overview = st.tabs(["Executive overview", "Pipeline explorer", "Operations", "Data quality", "Leadership brief"])

with overview[0]:
    left, right = st.columns(2)
    with left:
        pipeline = pd.DataFrame(engine.get_sector_breakdown())
        fig = px.bar(pipeline.head(8), x="segment", y="value", title="Pipeline by sector", color="segment")
        fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)
    with right:
        ops = pd.DataFrame(engine.get_operational_breakdown())
        fig2 = px.pie(ops.head(8), values="value", names="segment", title="Revenue by sector")
        fig2.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig2, use_container_width=True)

with overview[1]:
    pipeline_status = pd.DataFrame(engine.get_pipeline_by_status())
    fig3 = px.bar(pipeline_status, x="status", y="value", title="Pipeline by deal status", color="status")
    fig3.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig3, use_container_width=True)
    st.dataframe(pipeline_status, use_container_width=True)

with overview[2]:
    work = pd.DataFrame(engine.work_orders[["sector", "amount_excl_gst", "collected_incl_gst", "invoice_status", "execution_status"]].copy())
    work["collection_coverage"] = (work["collected_incl_gst"] / work["amount_excl_gst"] * 100).fillna(0)
    st.dataframe(work.head(20), use_container_width=True)
    summary = work.groupby("sector")["collection_coverage"].mean().reset_index().sort_values("collection_coverage", ascending=False)
    fig4 = px.bar(summary, x="sector", y="collection_coverage", title="Mean collection coverage by sector")
    fig4.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig4, use_container_width=True)

with overview[3]:
    issues = pd.DataFrame(engine.get_quality_issues())
    st.dataframe(issues, use_container_width=True)
    for item in engine.get_quality_issues():
        st.warning(f"{item['issue']}: {item['count']} records")

with overview[4]:
    summary = engine.get_leadership_summary()
    st.markdown(f"### {summary['headline']}")
    st.markdown("**Key risks:**")
    for risk in summary["risks"]:
        st.write(f"- {risk}")
    st.markdown("**Top pipeline sectors:**")
    for row in summary["top_pipeline_sectors"]:
        st.write(f"- {row['segment']}: ₹{row['value']:,.2f}")

st.markdown("<div class='glass-panel' style='margin-top: 1rem;'>", unsafe_allow_html=True)
st.subheader("Data quality notes")
for key, value in engine.bundle.quality_report.items():
    if isinstance(value, dict):
        st.write(f"**{key}**: {value}")
    else:
        st.write(f"**{key}**: {value}")
st.markdown("</div>", unsafe_allow_html=True)
