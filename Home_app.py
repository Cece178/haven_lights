#HOME PAGE (self defence videos)

import streamlit as st

st.set_page_config(page_title="Haven", page_icon="💗")

#gemini navgiation suggestion:
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home_app"

if st.session_state.current_page == "Home_app":
    col1, col2, col3 = st.columns([1, 2, 1])  # Adjust column widths as needed
    with col2:
        st.image("images/Haven_App_Logo_-_Technovations.png", width=320)
        st.markdown("<h1 style= 'text-align: center;'>💗Haven💗</h1>", unsafe_allow_html=True) 
elif st.session_state.current_page == "profile":
    st.write("Welcome to the Profile Page!")

# --- Scrollable Video Frame ---
st.markdown(
    """
    <style>
    .scrollable-videos {
        width: 100%;
        height: 80vh; /* Adjust height to fit your app layout */
        overflow-y: scroll; /* Enable vertical scrolling */
        border: 2px solid #F1587D; /* Optional: Add a border for styling */
        border-radius: 10px; /* Optional: Rounded corners */
        padding: 10px;
        background-color: #370A18; /* Optional: Background color */
    }

    .scrollable-videos::-webkit-scrollbar {
        width: 8px; /* Width of the scrollbar */
    }

    .scrollable-videos::-webkit-scrollbar-thumb {
        background-color: #F1587D; /* Scrollbar color */
        border-radius: 10px; /* Rounded scrollbar */
    }

    .video-container {
        margin-bottom: 20px; /* Add spacing between videos */
    }
    </style>
    <div class="scrollable-videos">
        <div class="video-container">
            <video controls width="100%">
                <source src="videos/IMG_5850.MOV" type="video/quicktime">
                Your browser does not support the video tag.
            </video>
        </div>
        <div class="video-container">
            <video controls width="100%">
                <source src="videos/IMG_5850.MOV" type="video/quicktime">
                Your browser does not support the video tag.
            </video>
        </div>
        <div class="video-container">
            <video controls width="100%">
                <source src="videos/IMG_5850.MOV" type="video/quicktime">
                Your browser does not support the video tag.
            </video>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# Redirect to the selected page
if st.session_state.current_page == "map":
    params = st.query_params  # Get current query parameters as a dictionary
    params["page"] = "map"  # Update the 'page' parameter
    st.query_params = params  # Set the query parameters
    st.stop()
