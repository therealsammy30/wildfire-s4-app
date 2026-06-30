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
st.write("---")
st.markdown("<h2 style='font-family: Arial, sans-serif; color: #1f2937; margin-top: 25px;'>Find Your Zone</h2>", unsafe_allow_html=True)
st.markdown("<p style='font-family: Arial, sans-serif; color: #4b563; font-size: 16px;'>Find your zone to view risk data, preparation checklists, and to be part of community discussions.</p>", unsafe_allow_html=True)
zone_col1, zone_col2 = st.columns(2)
with zone_col1:
    st.markdown("<h3 style='font-family: Arial, sans-serif; color: #1f2937; margin-top: 15px;'>Hills & Foothills</h3>", unsafe_allow_html=True)
    st.error("High Risk")
    st.markdown("<p style='font-family: Arial, sans-serif; color: #4b5563; margin-top: 5px;'> The hills and foothills are along Cupertino's western border and eventually meet the Santa Cruz Mountains. Steep canyons that tend to accelerate upward winds, and dry flammable vegetation causes this area to face extreme wildfire risk.</p>", unsafe_allow_html=True)