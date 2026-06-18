import streamlit as st
st.set_page_config(layout="wide")
st.markdown("<h3 style='font-family: Arial, sans-serif; color: #374151; margin-bottom: 0px;'>Cupertino Ready</h3>", unsafe_allow_html=True)
st.markdown("<h1 style='font-family: Arial, sans-serif; color: #1f2937; margin-top: 10px;'>Connect. Prepare. Stay Safe.</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-family: Arial, sans-serif; color: #4b5563; font-size: 16px;'>Cupertino's wildfire preparedness chat. Find your zone, track your readiness, and connect with your community.</p>", unsafe_allow_html=True)
st.write("")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="City Readiness", value="0%")
with col2:
    st.metric(label="Residents Engaged", value="0")
with col3:
    st.metric(label="High Risk Zones", value="2")
with col4:
    st.metric(label="Open Assembly Points", value="4 / 4")