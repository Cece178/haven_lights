#HOME PAGE (self defence videos)
import streamlit as st
st.set_page_config(page_title="Haven", page_icon="💗")

#gemini navgiation suggestion:
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home_app"

if st.session_state.current_page == "Home_app":
    col1, col2, col3 = st.columns([1, 2, 1]) 
    with col2:
        st.markdown("<h1 style= 'text-align: center;'>💖Welcome!💖</h1>", unsafe_allow_html=True) 
        st.image("images/Haven_App_Logo_-_Technovations.png", width=320)
        st.markdown("<h5 style= 'text-align: center;'>Example Videos (more coming soon!)</h1>", unsafe_allow_html=True)
elif st.session_state.current_page == "profile":
    st.write("Welcome to the Profile Page!")

#my code
st.video("videos/IMG_2862.MOV", loop=True, autoplay=True, end_time=8)
st.video("videos/IMG_2864.MOV", loop=True, end_time=3)
#end of my code

if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# Redirect to the selected page
if st.session_state.current_page == "map":
    params = st.query_params 
    params["page"] = "map"
    st.query_params = params 
    st.stop()
