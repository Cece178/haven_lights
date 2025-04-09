#my code with guidance from Gemini Copilot
import streamlit as st
import time 

#my code
col1, col2 = st.columns([1, 2])
with col2:
    st.image("images/Haven_App_Logo_-_Technovations.png", width=200)
#end of my code

if "button_pressed" not in st.session_state:
    st.session_state.button_pressed = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "timeout_expired" not in st.session_state:
    st.session_state.timeout_expired = False

timeout_duration = 30 # reduce for testing

if st.session_state.start_time is None:
    st.session_state.start_time = time.time()

button_container = st.empty()

if not st.session_state.button_pressed and not st.session_state.timeout_expired:
    st.markdown("<h4 style= 'text-align: center; color: pink'>🚨If you feel unsafe and want to alert your angels, click <strong>HELP ME</strong>. If you came here by accident, please <strong>DO NOT</strong> press the button. We will redirect you soon.🚨</h1>", unsafe_allow_html=True)
    
    with button_container:
        if st.button("HELP ME", use_container_width=True):
            st.session_state.button_pressed = True
            st.session_state.timeout_expired = True
            button_container.empty()
            st.rerun() 
   
    countdown_container = st.empty()

    remaining_time = timeout_duration - (time.time() - st.session_state.start_time)

    while remaining_time > 0:
        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)
        countdown_container.markdown(f"<h4 style='text-align: center; color: pink'>In <strong style='font-size: 36px; font-weight: bold'>{minutes:02d}:{seconds:02d}</strong> we will assume you are safe.</h4>", unsafe_allow_html=True)
        time.sleep(1)
        remaining_time = timeout_duration - (time.time() - st.session_state.start_time)

    st.session_state.timeout_expired = True
    st.rerun()

if st.session_state.timeout_expired and not st.session_state.button_pressed:
    st.toast("YAY!", icon="🥳")
    st.balloons()
    st.markdown("<h4 style='text-align: center; color: pink'>We're glad you're safe! Please return to the homepage. Take care! <em style='font-size: 20px'>Love, the Haven Lights</em></h4>", unsafe_allow_html=True)
    time.sleep(5) 
    st.switch_page("Home_app.py")

if st.session_state.button_pressed:
    st.markdown("<h4 style= 'text-align: center;'>Try not to engage unless necessary, it's best to avoid any confrontation. We have alerted your angels. Do you wish to alert the police? (Police alerts coming soon to the app!)</p>", unsafe_allow_html=True)
    if st.button("Please alert the police! I don't feel safe.", use_container_width= True):
        st.markdown("<h6 style= 'text-align: center;'>(Feature coming soon) We have alerted the police and sent them your location. Please stay aware of your surroundings. </h6>", unsafe_allow_html=True)
    #code from https://www.youtube.com/watch?v=UnjaSkrfWOs 
    audio_value = st.audio_input("Please start the recording by pressing the microphone")
    if audio_value:
        st.audio(audio_value)

        