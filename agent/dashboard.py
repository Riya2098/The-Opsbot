import streamlit as st

st.title("OpsBot DevOps AI Agent")

with open("rca.txt", "r") as f:
    rca = f.read()

with open("incident_logs.txt", "r") as f:
    logs = f.read()

st.subheader("Logs")
st.code(logs, language="bash")

st.subheader("Root Cause Analysis")
st.markdown(rca)
