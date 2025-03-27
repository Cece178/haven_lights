import streamlit as st

st.markdown("<h1 style='text-align: center;'>Haven Sleepwear Collection</h1>", unsafe_allow_html=True)

st.markdown('<p style="text-align: center;">add text here</p>', unsafe_allow_html=True)

cols = st.columns(4)
cols[0].image('images/pajama2.jpg')
cols[1].image('images/pajama3.jpg')
cols[2].image('images/pajama4.jpg')
cols[3].image('images/pajama5.jpg')

cols = st.columns(4)
cols[1].image('images/pajama2.jpg')
cols[2].image('images/pajama3.jpg')
cols[3].image('images/pajama4.jpg')
cols[4].image('images/pajama5.jpg')

cols = st.columns(4)
cols[1].image('images/pajama2.jpg')
cols[2].image('images/pajama3.jpg')
cols[3].image('images/pajama4.jpg')
cols[4].image('images/pajama5.jpg')