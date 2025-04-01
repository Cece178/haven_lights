#HOME PAGE (self defence videos)

import streamlit as st
import streamlit.components.v1 as components

# --- Setup ---
st.set_page_config(page_title="Haven", layout="wide")

st.markdown(
    """
    <style>
    body {
        background-color: #ffe4e1;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Custom CSS for Font and Icons ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Glacial+Indifference&display=swap');

    .title-container {
        display: flex;
        justify-content: center; /* Center the title */
        align-items: center;
    }

    .title-text {
        font-family: 'Glacial Indifference', sans-serif;
        font-size: 3em;
        font-weight: bold;
        margin: 0 20px; /* Increased space between icons and title */
    }

    .icon-button {
        background: none;
        border: none;
        padding: 0;
        margin: 0 20px; /* Increased space between icons and title */
        font-size: 1.5em; /* Adjust icon size */
    }

    .video-frame {
        width: 100%;
        height: 500px; /* Adjust height as needed */
        overflow-y: scroll;
        border: 1px solid #ccc;
        margin-top: 20px;
    }

    .bottom-icons {
        display: flex;
        justify-content: space-around;
        margin-top: 20px;
    }

    .bottom-icons button {
        background: none;
        border: none;
        font-size: 1.5em;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Title and Icon Buttons ---
col1, col2, col3 = st.columns([1, 4, 1])

with col1:
    if st.button("🪙", key="coin_button", help="Coin Page"):
        st.write("Coin page clicked!") # replace with page nav

with col2:
    st.markdown('<div class="title-container"><span class="title-text">Haven</span></div>', unsafe_allow_html=True)

with col3:
    if st.button("💬", key="speech_button", help="Chat Page"):
        st.write("Chat page clicked!") # replace with page nav

# --- Video Frame ---
st.markdown('<div class="video-frame">', unsafe_allow_html=True)
st.video("https://youtube.com/shorts/VjUmmOZX27g?si=_vErDxoOl-rJFw_T") # Replace with your YouTube URL
st.video("https://youtube.com/shorts/HGmQcmOqLMs?si=2pMkcJz2xUITCG3o") # Replace with your YouTube URL
st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .video-frame {
        width: 100%;
        height: 80vh; /* Make it fill most of the vertical height */
        overflow-y: scroll;
        border: 1px solid #ccc;
        margin-top: 20px;
        display: flex;
        flex-direction: column; /* Stack videos vertically */
    }

    .video-frame video {
        width: 100%; /* Make videos fill the frame width */
        height: auto; /* Maintain aspect ratio */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Custom CSS for Bottom Icons ---
st.markdown(
    """
    <style>
    .bottom-icons {
        display: flex;
        justify-content: center; # Center the buttons
        margin-top: 20px;
    }

    .bottom-icons button {
        background: none;
        border: none;
        font-size: 1.5em;
        padding: 10px;
        margin: 0 10px; # Add some horizontal spacing between buttons
    }

    .exclamation-button {
        background-color: #f1587d;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🏠", key="home_button"):
        st.session_state.current_page = "home"

with col2:
    if st.button("🕊️", key="wings_button"):
        st.session_state.current_page = "wings"

with col3:
    if st.button("❗", key="exclamation_button"):
        st.session_state.current_page = "exclamation"

with col4:
    if st.button("🗺️", key="map_button"):
        st.session_state.current_page = "map"

with col5:
    if st.button("👤", key="person_button"):
        st.session_state.current_page = "person"

# Redirect to the selected page
if st.session_state.current_page == "map":
    params = st.query_params  # Get current query parameters as a dictionary
    params["page"] = "map"  # Update the 'page' parameter
    st.query_params = params  # Set the query parameters
    st.stop()