import streamlit as st

st.set_page_config(layout="wide", page_title="Cupertino Ready")

# 1. APP MEMORY ENGINE & SCORE CALCULATORS
if "page" not in st.session_state:
    st.session_state.page = "main"

# Hidden tracking lists to remember which tasks you checked off across all pages
if "checked_hills" not in st.session_state:
    st.session_state.checked_hills = [False, False, False]
if "checked_creek" not in st.session_state:
    st.session_state.checked_creek = [False, False, False]
if "checked_central" not in st.session_state:
    st.session_state.checked_central = [False, False, False]
if "checked_north" not in st.session_state:
    st.session_state.checked_north = [False, False, False]
if "checked_east" not in st.session_state:
    st.session_state.checked_east = [False, False, False]

def go_to_page(page_name):
    st.session_state.page = page_name

# Calculate dynamic statistics across the entire city based on live checkmarks
total_possible_tasks = 15
total_done_tasks = (
    sum(st.session_state.checked_hills) + sum(st.session_state.checked_creek) +
    sum(st.session_state.checked_central) + sum(st.session_state.checked_north) +
    sum(st.session_state.checked_east)
)
city_readiness_percentage = int((total_done_tasks / total_possible_tasks) * 100)

# 2. MAIN LANDING DASHBOARD GRID VIEW
if st.session_state.page == "main":
    st.markdown("<h3 style='font-family: Arial, sans-serif; color: #374151; margin-bottom: 0px;'>Cupertino Ready</h3>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-family: Arial, sans-serif; color: #1f2937; margin-top: 10px;'>Connect. Prepare. Stay Safe.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-family: Arial, sans-serif; color: #4b5563; font-size: 16px;'>Cupertino's wildfire preparedness platform. Find your zone, track your readiness, and connect with your neighborhood.</p>", unsafe_allow_html=True)
    st.write("")

    # Dynamic metrics connected directly to the user's progress
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="City Readiness", value=f"{city_readiness_percentage}%")
    with col2:
        st.metric(label="Tasks Completed", value=f"{total_done_tasks} / 15")
    with col3:
        st.metric(label="High Risk Zones Listed", value="2")
    with col4:
        st.metric(label="Open Assembly Points", value="4 / 4")
    st.write("---")

    st.markdown("<h2 style='font-family: Arial, sans-serif; color: #1f2937; margin-top: 25px;'>Find Your Zone</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-family: Arial, sans-serif; color: #4b5563; font-size: 16px;'>Select your community area to complete safety checklists and access local discussion updates.</p>", unsafe_allow_html=True)

    zone_col1, zone_col2 = st.columns(2)
    with zone_col1:
        st.markdown("<h3 style='font-family: Arial, sans-serif; color: #1f2937; margin-top: 15px;'>Hills & Foothills</h3>", unsafe_allow_html=True)
        st.error("High Risk")
        st.markdown("<p style='font-family: Arial, sans-serif; color: #4b5563; margin-top: 5px;'>Western hillside border zone meeting the Santa Cruz Mountains. Steep canyon layout speeds up winds with extreme dry brush conditions.</p>", unsafe_allow_html=True)
        if st.button("Open Hills Hub", key="btn_hills", on_click=go_to_page, args=("Hills & Foothills",)):
            st.rerun()

    with zone_col2:
        st.markdown("<h3 style='font-family: Arial, sans-serif; color: #1f2937; margin-top: 15px;'>Stevens Creek Corridor</h3>", unsafe_allow_html=True)
        st.error("High Risk")
        st.markdown("<p style='font-family: Arial, sans-serif; color: #4b5563; margin-top: 5px;'>Areas surrounding Stevens Creek. Dense foliage vegetation with restricted road outlet paths requires cautious evacuation planning.</p>", unsafe_allow_html=True)
        if st.button("Open Stevens Creek Hub", key="btn_stevens", on_click=go_to_page, args=("Stevens Creek Corridor",)):
            st.rerun()

    zone_col3, zone_col4 = st.columns(2)
    with zone_col3:
        st.markdown("<h3 style='font-family: Arial, sans-serif; color: #1f2937; margin-top: 15px;'>Central Cupertino</h3>", unsafe_allow_html=True)
        st.warning("Medium Risk")
        st.markdown("<p style='font-family: Arial, sans-serif; color: #4b5563; font-size: 14px; margin-top: 5px;'>Residential and business core including Downtown. Minor direct flame paths but serves as a central smoke safety checkpoint.</p>", unsafe_allow_html=True)
        if st.button("Open Central Hub", key="btn_central", on_click=go_to_page, args=("Central Cupertino",)):
            st.rerun()

    with zone_col4:
        st.markdown("<h3 style='font-family: Arial, sans-serif; color: #1f2937; margin-top: 15px;'>North Cupertino</h3>", unsafe_allow_html=True)
        st.warning("Medium Risk")
        st.markdown("<p style='font-family: Arial, sans-serif; color: #4b5563; font-size: 14px; margin-top: 5px;'>Neighborhood areas near Sunnyvale borders. Insulated from forest paths but susceptible to windblown ash hazards.</p>", unsafe_allow_html=True)
        if st.button("Open North Hub", key="btn_north", on_click=go_to_page, args=("North Cupertino",)):
            st.rerun()

    zone_col5 = st.columns(1)
    with zone_col5[0]:
        st.markdown("<h3 style='font-family: Arial, sans-serif; color: #1f2937; margin-top: 15px;'>East Cupertino</h3>", unsafe_allow_html=True)
        st.success("Low Risk")
        st.markdown("<p style='font-family: Arial, sans-serif; color: #4b5563; font-size: 14px; margin-top: 5px;'>Flat terrain adjacent to San Jose. Safest relative geographic zone primarily utilized for evacuation shelter bases.</p>", unsafe_allow_html=True)
        if st.button("Open East Hub", key="btn_east", on_click=go_to_page, args=("East Cupertino",)):
            st.rerun()

# 3. INTERACTIVE SUB-PAGE COMMUNITY HUBS VIEW
else:
    if st.button("⬅️ Back to Dashboard"):
        go_to_page("main")
        st.rerun()

    st.write(f"### Welcome to the {st.session_state.page} Community Hub")
    st.write("Complete your localized preparation plan to increase the overall City Readiness Score!")
    st.write("---")

    # Map hidden session states to the active open screen view
    if st.session_state.page == "Hills & Foothills":
        current_list = "checked_hills"
    elif st.session_state.page == "Stevens Creek Corridor":
        current_list = "checked_creek"
    elif st.session_state.page == "Central Cupertino":
        current_list = "checked_central"
    elif st.session_state.page == "North Cupertino":
        current_list = "checked_north"
    else:
        current_list = "checked_east"

    # Dynamic Task System that remembers your work
    st.markdown("<h4 style='font-family: Arial, sans-serif; color: #1f2937;'>Your Safety Requirements</h4>", unsafe_allow_html=True)
    
    st.session_state[current_list][0] = st.checkbox("Clear dry vegetation within 30 feet of your property lines.", value=st.session_state[current_list][0])
    st.session_state[current_list][1] = st.checkbox("Assemble a 3-day rapid evacuation supply Go-Bag.", value=st.session_state[current_list][1])
    st.session_state[current_list][2] = st.checkbox("Register emergency contacts with regional ReadySCC alert databases.", value=st.session_state[current_list][2])

    # Score calculation engine inside the active screen view
    page_done = sum(st.session_state[current_list])
    st.progress(page_done / 3)

    if page_done == 3:
        st.balloons()
        st.success("🎉 Zone completely ready! Your completion points have updated the city dashboard metrics!")
    elif page_done > 0:
        st.warning(f"⚠️ Progress recorded. {page_done}/3 requirements fulfilled.")
    else:
        st.info("💡 Complete the checklist items above to secure your household.")

    # Localized Neighborhood Forums
    st.write("---")
    st.markdown("<h4 style='font-family: Arial, sans-serif; color: #1f2937;'>Live Area Notice Board</h4>", unsafe_allow_html=True)
    st.chat_message("user").write(f"**Resident Mark:** Clearing brush along the driveway today. Stay safe everyone in {st.session_state.page}!")
    st.chat_message("assistant").write("**Zone Warden Info:** Ensure vehicle fuel tanks are filled in preparation for changing seasonal wind alerts.")

    # Live Mapping Layout Canvas
    st.write("---")
    st.markdown("<h4 style='font-family: Arial, sans-serif; color: #1f2937;'>Area Evacuation Routes & Gathering Spots</h4>", unsafe_allow_html=True)
    st.map()
    st.caption("🗺️ Interactive area positioning displays active escape route pathways, safe streets, and Cupertino response sectors.")


