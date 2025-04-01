
#my code with guidance from Gemini Copilot
import streamlit as st
import time 


#from video https://www.youtube.com/watch?v=hEPoto5xp3k
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "Guardian Angels", "Map", "Profile"],
        icons=["house", "arrow-through-heart", "map", "person"],
        default_index=0,
        orientation="vertical",
        styles={
            "icon": {"color": "pink", "font-size": "25px"},
        }
    )

    if selected == "Home":
        st.switch_page("real_home_page.py")
    if selected == "Guardian Angels":
        st.switch_page("guardian_angels_page.py")
    if selected == "Map":
        st.switch_page("map_page.py")
    if selected == "Profile":
        st.switch_page("messages.py")

#end of video code

if "button_pressed" not in st.session_state:
    st.session_state.button_pressed = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "timeout_expired" not in st.session_state:
    st.session_state.timeout_expired = False

timeout_duration = 5 # reduce for testing

if st.session_state.start_time is None:
    st.session_state.start_time = time.time()

if not st.session_state.button_pressed and not st.session_state.timeout_expired:
    st.markdown("<h4 style= 'text-align: center; color: pink'>🚨If you feel unsafe and want to alert your angels, click <strong>HELP ME</strong>. If you came here by accident, please <strong>DO NOT</strong> press the button. We will redirect you soon.🚨</h1>", unsafe_allow_html=True)

    remaining_time = timeout_duration - (time.time() - st.session_state.start_time)

    if remaining_time > 0:
        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)
        st.markdown(f"<h4 style='text-align: center;'>In: <strong>{minutes:02d}:{seconds:02d}</strong> we will assume you are safe.</h4>", unsafe_allow_html=True)
    else:
        st.session_state.timeout_expired = True
        st.rerun()

    if st.button("HELP ME", use_container_width=True):
        st.session_state.button_pressed = True
        st.rerun()

if st.session_state.timeout_expired and not st.session_state.button_pressed:
    st.markdown("<h4 style='text-align: center;'>We're glad you're safe! Please return to the homepage. Take care! <em>Love, the Haven Lights</em></h4>", unsafe_allow_html=True)
    time.sleep(2)  # Wait for 2 seconds before redirecting
    st.switch_page("real_home_page.py") #ask peoples why it isn't working and/or just use sidebar

if st.session_state.button_pressed:
    st.markdown("<h4 style= 'text-align: center;'>Take deep breaths. Try not to engage unless necessary, it's best to avoid any confrontation. We have alerted your angels. Do you wish to alert the police?</p>", unsafe_allow_html=True)
    if st.button("Please alert the police! I don't feel safe.", use_container_width= True):
        st.markdown("<h6 style= 'text-align: center;'>We have alerted the police and sent them your location. Please stay aware of your surroundings. We are taking care of it. You are not alone. </h6>", unsafe_allow_html=True)
