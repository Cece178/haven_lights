import streamlit as st #start of my code (with some guidance from Gemini)

st.markdown("<h1 style='text-align: center; margin-bottom: 0.001em'>Your Guardian Angels</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Meet your angels!</h2>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; margin-bottom: 0.01em'>Your primary angels are marked with a 💖</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; margin-top: 0.01em'>All other angels are 🪽</p>", unsafe_allow_html=True)
#end of my code

#start of Gemini code
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        text-align:center;
        width:100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
    .button-container {
        background-image: url("main_app/images/gradient_pink.jpg") !important;
        background-size: cover !important;
        background-repeat: no-repeat !important;
        padding: 20px !important;
    }
    .stButton > button:first-child {
        text-align:center;
        width:100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
#end of Gemini code

with st.container(): #start of Gemini code
    st.markdown('<div class="button-container">', unsafe_allow_html=True) #end of Gemini code
    st.button("Selene💖 ––→  3km away") #start of my code
    st.button("Dad💖 ––→  5km away")
    st.button("Mom💖 ––→  10km away")
    st.button("Leah🪽 ––→  2km away")
    st.button(" Add another angel☁️") #end of my code
    st.markdown('</div>', unsafe_allow_html=True) #line of Gemini code

#start of Gemini code
# --- Bottom Navigation Buttons ---
st.markdown('<div class="bottom-nav">', unsafe_allow_html=True)  
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🏠", key="home_button"):
        st.session_state.current_page = "home"
        st.rerun()

with col2:
    if st.button("🕊️", key="wings_button"):
        st.session_state.current_page = "wings"
        st.rerun()

with col3:
    if st.button("❗", key="exclamation_button"):
        st.session_state.current_page = "exclamation"
        st.rerun()

with col4:
    if st.button("🗺️", key="map_button"):
        st.session_state.current_page = "map"
        st.rerun()

with col5:
    if st.button("👤", key="person_button"):
        st.session_state.current_page = "person"
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)  # Close the bottom nav container

if st.session_state.current_page == "home":
    st.Page("main_app/streamlit_app.py")
elif st.session_state.current_page == "wings":
    st.Page("guardian_angels_page.py")
elif st.session_state.current_page == "exclamation":
    st.header("Exclamation Page")
elif st.session_state.current_page == "map":
    st.header("Map Page")
if st.session_state.current_page == "person":
    st.Page("messages.py")
#end of Gemini code
