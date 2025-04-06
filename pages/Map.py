#start of my code
import streamlit as st

#my code
st.markdown("<h1 style= 'text-align: center; margin-bottom: 0.01em'>🗺️   Map   🗺️</h1>", unsafe_allow_html=True)
st.markdown("<h3 style= 'text-align: center; color: pink'>Always know where your angels are</h2>", unsafe_allow_html=True)
st.markdown("<p style= 'text-align: center; color: pink; margin-bottom: 2em'>Your angels will be displayed like this:😇 and your safe spots will be displayed like this:☁️</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2, vertical_alignment="center")

with col1:
    st.button("add a safe spot ☁️", use_container_width=True)

with col2:
    st.button("add an angel 😇", use_container_width=True)

st.image('images/map-placeholder.jpg')


if st.button("🏠"):
    st.switch_page("../main_app/streamlit_app.py")

if st.button("🪽"):
    st.switch_page("guardian_angels_page.py")

if st.button("🗺️"):
    st.switch_page("map_page.py")

if st.button("😎"):
    st.switch_page("/*add page here*/")
#end of my code
