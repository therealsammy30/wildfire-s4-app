import streamlit as st

st.set_page_config(layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "main"

def go_to_page(page_name):
    st.session_state.page = page_name

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
st.markdown("<p style='font-family: Arial, sans-serif; color: #4b5563; font-size: 16px;'>Find your zone to view risk data, preparation checklists, and to be part of community discussions.</p>", unsafe_allow_html=True)

zone_col1, zone_col2 = st.columns(2)
with zone_col1:
    st.markdown("<h3 style='font-family: Arial, sans-serif; color: #1f2937; margin-top: 15px;'>Hills & Foothills</h3>", unsafe_allow_html=True)
    st.error("High Risk")
    st.markdown("<p style='font-family: Arial, sans-serif; color: #4b5563; margin-top: 5px;'> The hills and foothills are along Cupertino's western border and eventually meet the Santa Cruz Mountains. Steep canyons that tend to accelerate upward winds, and dry flammable vegetation causes this area to face extreme wildfire risk.</p>", unsafe_allow_html=True)
    if st.button("Open Hills Hub", key="btn_hills", on_click=go_to_page, args=("Hills & Foothills",)):
        st.info("Entering the Hills/Foothills Community Board")

with zone_col2:
    st.markdown("<h3 style='font-family: Arial, sans-serif; color: #1f2937; margin-top: 15px;'>Stevens Creek Corridor</h3>", unsafe_allow_html=True)
    st.error("High Risk")
    st.markdown("<p style='font-family: Arial, sans-serif; color: #4b5563; margin-top: 5px;'>Areas that are adjacent to Stevens Creek and the surrounding open space. With dense dry brush and limited escape routes, this area of Cupertino is a high wildfire risk area.</p>", unsafe_allow_html=True)
    if st.button("Open Stevens Creek Hub", key="btn_stevens", on_click=go_to_page, args=("Stevens Creek Corridor",)):
        st.info("Entering the Stevens Creek Corridor Community Board")

zone_col3, zone_col4 = st.columns(2)
with zone_col3:
    st.markdown("<h3 style='font-family: Arial, sans-serif; color: #1f2937; margin-top: 15px;'>Central Cupertino</h3>", unsafe_allow_html=True)
    st.warning("Medium Risk")
    st.markdown("<p style='font-family: Arial, sans-serif; color: #4b5563; font-size: 14px; margin-top: 5px;'>The residential and commercial core, including Downtown Cupertino. This area has a lower direct fire risk but it is important for coordinating evacuation routes and smoke safety.</p>", unsafe_allow_html=True)
    if st.button("Open Central Hub", key="btn_central", on_click=go_to_page, args=("Central Cupertino",)):
        st.info("Entering the Central Cupertino Community Board")

with zone_col4:
    st.markdown("<h3 style='font-family: Arial, sans-serif; color: #1f2937; margin-top: 15px;'>North Cupertino</h3>", unsafe_allow_html=True)
    st.warning("Medium Risk")
    st.markdown("<p style='font-family: Arial, sans-serif; color: #4b5563; font-size: 14px; margin-top: 5px;'>The northern neighborhoods bordering Sunnyvale and Santa Clara. Lower direct wildfire threats, but heavily impacted by regional wildfire smoke and air quality hazards.</p>", unsafe_allow_html=True)
    if st.button("Open North Hub", key="btn_north", on_click=go_to_page, args=("North Cupertino",)):
        st.info("Entering the North Cupertino Community Board")

zone_col5 = st.columns(1)
with zone_col5[0]:
    st.markdown("<h3 style='font-family: Arial, sans-serif; color: #1f2937; margin-top: 15px;'>East Cupertino</h3>", unsafe_allow_html=True)
    st.success("Low Risk")
    st.markdown("<p style='font-family: Arial, sans-serif; color: #4b5563; font-size: 14px; margin-top: 5px;'>The eastern residential flatlands bordering San Jose and Saratoga. Eastern Cupertino has the lowest direct wildfire exposure, and it poses primarily as a safe destination for evacuating neighbors.</p>", unsafe_allow_html=True)
    if st.button("Open East Hub", key="btn_east", on_click=go_to_page, args=("East Cupertino",)):
        st.info("Entering the East Cupertino Community Board")

if st.session_state.page == "main":
    pass
else:
    if st.button("⬅️ Back to Dashboard"):
        st.session_state.page = "main"
        st.rerun()

if st.session_state.page != "main":
    st.write(f"### Welcome to the {st.session_state.page.replace('_',' ').title()}")
    st.write("Community preparedness checklists and localized risk safety discussions will load here!")
    st.markdown("<h4 style='font-family: Arial, sans-serif; color: #1f2937; margin-top: 20px;'>Your Zone Checklist</h4>", unsafe_allow_html=True)
    task1 = st.checkbox("Clear dry vegetation within 30 feet of your home (Defensible Space)")
    task2 = st.checkbox("Pack an emergency Go-Bag with 3 days of water, food, and vital documents")
    task3 = st.checkbox("Sign up for local county alerts (ReadySCC emergency notifications)")
    completed_tasks = sum([task1, task2, task3])
    st.progress(completed_tasks / 3)
    st.markdown("<h4 style='font-family: Arial, sans-serif; color: #1f2937; margin-top: 30px;'>Community Board Updates</h4>", unsafe_allow_html=True)
    st.chat_message("user").write("**Neighbor Dave:** Just finished clearing the dry brush from my front driveway slope. Anyone need help moving trimmings?")
    st.chat_message("assistant").write("**Zone Warden Sarah:** Extreme fire weather warning issued for tomorrow afternoon. Please double-check your Go-Bags tonight!")
    