#start of my code
import streamlit as st

st.markdown("<h1 style= 'text-align: center; margin-bottom: 0.01em'>🗺️   Map   🗺️</h1>", unsafe_allow_html=True)
st.markdown("<h3 style= 'text-align: center;'>Always know where your angels are</h2>", unsafe_allow_html=True)
st.markdown("<p style= 'text-align: center; margin-bottom: 2em'>Your angels will be displayed like this:😇 and your safe spots will be displayed like this:☁️</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2, vertical_alignment="center")

with col1:
    st.button("add a safe spot ☁️", use_container_width=True)

with col2:
    st.button("add an angel 😇", use_container_width=True)

st.image('main_app/images/map-placeholder.jpg')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.button("🏠", use_container_width=True)

with col2:
    st.button("🪽", use_container_width=True)

with col3:
    st.button("❕", use_container_width=True)

with col4:
    st.button("🗺️", use_container_width=True)

with col5: 
    st.button("😎", use_container_width=True)
#end of my code
