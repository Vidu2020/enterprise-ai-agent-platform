import streamlit as st
import json

st.set_page_config(
    page_title="Incident Details",
    page_icon="🎫",
    layout="wide"
)

st.title("🎫 Incident Details")

ticket_id = st.session_state.get(
    "selected_ticket"
)

if not ticket_id:
    st.warning("No ticket selected.")
    st.stop()

try:
    with open("logs/incident_logs.json", "r") as f:
        logs = json.load(f)

except (FileNotFoundError, json.JSONDecodeError):
    st.error("No incident data found.")
    st.stop()

incident = next(
    (
        item
        for item in logs
        if item["ticket_id"] == ticket_id
    ),
    None
)

if not incident:
    st.error("Incident not found.")
    st.stop()

st.subheader("🎫 Ticket Number")
st.code(incident["ticket_id"])

st.subheader("🕒 Timestamp")
st.write(
    incident.get("timestamp", "N/A")
)

st.subheader("📝 Reported Issue")
st.write(
    incident.get("issue", "N/A")
)

col1, col2 = st.columns(2)

with col1:

    st.subheader("🎯 Intent Agent")
    st.info(
        incident.get("intent", "")
    )

    st.subheader("📚 Knowledge Agent")
    st.success(
        incident.get("solution", "")
    )

with col2:

    st.subheader("👔 Manager Copilot")
    st.markdown(
        incident.get("summary", "")
    )

if st.button("⬅ Back to History"):
    st.switch_page(
        "pages/1_Incident_History.py"
    )