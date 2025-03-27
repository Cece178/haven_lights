#start of my code
import streamlit as st

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
        st.page_link("main_app/streamlit_app.py")
    if selected == "Guardian Angels":
        st.page_link("pages/guardian_angels_page.py")
    if selected == "Map":
        st.page_link("pages/map_page.py")
    if selected == "Profile":
        st.page_link("pages/disguise_home_page.py")

#end of video code

#my code
st.markdown("<h1 style= 'text-align: center; margin-bottom: 0.01em'>🗺️   Map   🗺️</h1>", unsafe_allow_html=True)
st.markdown("<h3 style= 'text-align: center;'>Always know where your angels are</h2>", unsafe_allow_html=True)
st.markdown("<p style= 'text-align: center; margin-bottom: 2em'>Your angels will be displayed like this:😇 and your safe spots will be displayed like this:☁️</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2, vertical_alignment="center")

with col1:
    st.button("add a safe spot ☁️", use_container_width=True)

with col2:
    st.button("add an angel 😇", use_container_width=True)

st.image('main_app/images/map-placeholder.jpg')


if st.button("🏠"):
    st.switch_page("../main_app/streamlit_app.py")

if st.button("🪽"):
    st.switch_page("guardian_angels_page.py")

if st.button("🗺️"):
    st.switch_page("map_page.py")

if st.button("😎"):
    st.switch_page("/*add page here*/")
#end of my code
