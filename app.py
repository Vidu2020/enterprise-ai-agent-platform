import streamlit as st
import json

from utils.logger import log_incident
from agents.intent_agent import detect_intent
from agents.knowledge_agent import get_solution
from agents.execution_agent import create_incident
from agents.manager_agent import generate_summary

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Enterprise AI Agent Platform",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# Sidebar Dashboard
# --------------------------------------------------

st.sidebar.header("📊 Dashboard")

try:

    with open(
        "incident_logs.json",
        "r",
        encoding="utf-8"
    ) as f:

        logs = json.load(f)

    st.sidebar.metric(
        "Total Incidents",
        len(logs)
    )

    if logs:

        st.sidebar.metric(
            "Latest Ticket",
            logs[-1].get(
                "ticket_id",
                "N/A"
            )
        )

except Exception:

    logs = []

    st.sidebar.metric(
        "Total Incidents",
        0
    )

# --------------------------------------------------
# Navigation
# --------------------------------------------------

st.sidebar.divider()

st.sidebar.page_link(
    "pages/1_Incident_History.py",
    label="📋 Incident History"
)

# --------------------------------------------------
# Main Page
# --------------------------------------------------

st.title("🤖 Enterprise AI Agent Platform")

st.markdown(
    """
    ### AI-Powered Incident Management Platform

    Features:

    - Gemini AI
    - Multi-Agent Architecture
    - Automated Incident Processing
    - Incident Analytics
    - Airflow Workflow Orchestration
    """
)

issue = st.text_area(
    "Describe Issue",
    placeholder="Example: VPN not working",
    key="issue_text"
)

# --------------------------------------------------
# Buttons
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    run_btn = st.button(
        "🚀 Run Agents",
        type="primary",
        use_container_width=True
    )

with col2:

    reset_btn = st.button(
        "🔄 Reset",
        use_container_width=True
    )

# --------------------------------------------------
# Reset
# --------------------------------------------------

if reset_btn:

    for key in list(st.session_state.keys()):

        del st.session_state[key]

    st.rerun()

# --------------------------------------------------
# Run Agents
# --------------------------------------------------

if run_btn:

    if not issue.strip():

        st.warning(
            "Please enter an issue description."
        )

        st.stop()

    try:

        with st.spinner(
            "Running AI Agents..."
        ):

            # Intent Agent

            intent = detect_intent(
                issue
            )

            # Knowledge Agent

            solution = get_solution(
                issue
            )

            # Execution Agent

            ticket = create_incident()

            # Manager Agent

            summary = generate_summary(
                issue=issue,
                ticket_id=ticket,
                intent_result=intent,
                solution=solution
            )

            # Logging

            log_incident(
                ticket_id=ticket,
                issue=issue,
                intent=intent,
                solution=solution,
                summary=summary
            )

        st.success(
            "✅ Analysis Complete"
        )

        # --------------------------------------------------
        # Issue
        # --------------------------------------------------

        st.subheader(
            "📝 Reported Issue"
        )

        st.write(issue)

        st.divider()

        # --------------------------------------------------
        # Results
        # --------------------------------------------------

        left, right = st.columns(2)

        with left:

            st.subheader(
                "🎯 Intent Agent"
            )

            st.info(intent)

            st.subheader(
                "📚 Knowledge Agent"
            )

            st.success(solution)

        with right:

            st.subheader(
                "🎫 Execution Agent"
            )

            st.code(ticket)

            st.subheader(
                "👔 Manager Copilot"
            )

            st.markdown(summary)

    except Exception as e:

        st.error(
            f"❌ Error: {str(e)}"
        )

# --------------------------------------------------
# Recent Incidents
# --------------------------------------------------

st.divider()

st.subheader("📝 Recent Incidents")

if logs:

    for incident in reversed(logs[-5:]):

        with st.expander(
            incident.get(
                "ticket_id",
                "Unknown Ticket"
            )
        ):

            st.write(
                f"**Issue:** {incident.get('issue', '')}"
            )

            st.write(
                f"**Solution:** {incident.get('solution', '')}"
            )

            st.write(
                f"**Timestamp:** {incident.get('timestamp', '')}"
            )

else:

    st.info(
        "No incidents logged yet."
    )