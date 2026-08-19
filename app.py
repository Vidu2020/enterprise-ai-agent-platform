import streamlit as st
import json

from utils.logger import log_incident
from agents.intent_agent import detect_intent
from agents.knowledge_agent import get_solution
from agents.execution_agent import create_ticket
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
    with open("logs/incident_logs.json", "r") as f:
        logs = json.load(f)

    st.sidebar.metric(
        "Total Incidents",
        len(logs)
    )

    if logs:
        st.sidebar.metric(
            "Latest Ticket",
            logs[-1].get("ticket_id", "N/A")
        )

except (FileNotFoundError, json.JSONDecodeError):
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

issue = st.text_area(
    "Describe Issue",
    placeholder="Example: VPN not working",
    key="issue_text"
)

# --------------------------------------------------
# Buttons
# --------------------------------------------------

btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    run_btn = st.button(
        "Run Agents",
        type="primary",
        use_container_width=True
    )

with btn_col2:
    reset_btn = st.button(
        "Reset",
        use_container_width=True
    )

# --------------------------------------------------
# Reset Button
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
        st.warning("Please enter an issue description.")
        st.stop()

    try:

        with st.spinner("Running AI Agents..."):

            # Intent Agent
            intent = detect_intent(issue)

            # Knowledge Agent
            solution = get_solution(issue)

            # Execution Agent
            ticket = create_ticket()

            # Manager Copilot
            summary = generate_summary(
                intent,
                solution,
                ticket
            )

            # Log Incident
            log_incident(
                ticket,
                issue,
                intent,
                solution,
                summary
            )

        st.success("✅ Analysis Complete")

        # --------------------------------------------------
        # Reported Issue
        # --------------------------------------------------

        st.subheader("📝 Reported Issue")
        st.write(issue)

        st.divider()

        # --------------------------------------------------
        # Results
        # --------------------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("🎯 Intent Agent")
            st.info(intent)

            st.subheader("📚 Knowledge Agent")
            st.success(solution)

        with col2:

            st.subheader("🎫 Execution Agent")
            st.code(ticket)

            st.subheader("👔 Manager Copilot")
            st.markdown(summary)

    except Exception as e:

        st.error(
            f"❌ Error: {str(e)}"
        )