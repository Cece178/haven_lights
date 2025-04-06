import streamlit as st

st.markdown("<h5 style = 'text-align: center;'>welcome to the the testing page!</h6>", unsafe_allow_html=True)

st.markdown("<h1 style = 'text-align: center;'>😱</h6>", unsafe_allow_html=True)

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