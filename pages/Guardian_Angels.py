import streamlit as st #start of my code (with some guidance from Gemini)

st.markdown("<h1 style='text-align: center; margin-bottom: 0.001em'>😇Your Guardian Angels😇</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: pink'>Meet your angels!</h2>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; margin-bottom: 0.01em; color: pink'>Your primary angels are marked with a 💖</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; margin-top: 0.01em; color: pink'>All other angels are 🪽</p>", unsafe_allow_html=True)
#end of my code

#start of Gemini code
if 'angel_buttons' not in st.session_state:
    st.session_state.angel_buttons = [
        "Selene💖 ––→  3km away",
        "Dad💖 ––→  5km away",
        "Mom💖 ––→  10km away",
        "Leah🪽 ––→  2km away"
    ]

if 'new_angel_name' not in st.session_state:
    st.session_state.new_angel_name = ""
if 'new_angel_distance' not in st.session_state:
    st.session_state.new_angel_distance = ""

new_angel_name = st.text_input("Angel Name", placeholder= "Add name of your angel here", key="angel_name", value=st.session_state.new_angel_name)
new_angel_distance = st.text_input("Distance (km)", placeholder= "Real-time location updates will be functional soon, so stay on the lookout for updates!", key="angel_distance", value=st.session_state.new_angel_distance)

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

def add_angel():
    if new_angel_name and new_angel_distance:
        new_angel_button = f"{new_angel_name}🪽 ––→  {new_angel_distance}km away"
        st.session_state.angel_buttons.append(new_angel_button)
        st.session_state.new_angel_name = ""
        st.session_state.new_angel_distance = ""

if st.button("Add angel☁️", on_click=add_angel):
    pass
    st.toast("Angel added!", icon="💖")

with st.container():
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    for angel_button in st.session_state.angel_buttons:
        st.button(angel_button)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<p style='text-align: center; margin-top: 0.01em; color: pink'>Coming soon: Click on an angel to find them on the map!</p>", unsafe_allow_html=True)