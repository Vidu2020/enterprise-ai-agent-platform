import streamlit as st
import json
import pandas as pd

st.set_page_config(
    page_title="Incident History",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Incident History")

try:
    with open("logs/incident_logs.json", "r") as f:
        logs = json.load(f)

except Exception as e:
    st.error(f"Error reading logs: {e}")
    st.stop()

# Debug
st.write(f"Records Loaded: {len(logs)}")

if not logs:
    st.warning("No incidents found.")
    st.stop()

# Convert to dataframe
df = pd.DataFrame(logs)

st.dataframe(
    df,
    use_container_width=True
)