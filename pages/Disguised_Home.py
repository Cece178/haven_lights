#my code
import streamlit as st
st.set_page_config(page_title="Haven Sleepwear", page_icon="💗")


if st.button("🪙", type = 'tertiary'):
    st.switch_page("Home_app.py")

st.toast("Updates coming soon to this page!", icon="✨")
st.toast("Click the coin on the left side of the page for a quick way to leave the diguised home page!", icon="ℹ️")

st.markdown("<h1 style='text-align: center;'>💤Haven Sleepwear💤</h1>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; color: pink; margin-bottom: 0.0001em'>Sleep Like A Baby Collection</p>", unsafe_allow_html=True)

cols = st.columns(7)
cols[0].button("Gowns")
cols[1].button("Onesies")
cols[2].button("Summer")
cols[3].button("Winter")
cols[4].button("Cotton")
cols[5].button("Silk")
cols[6].button("Lounge")

st.markdown("<h4 style='text-align: left; color: pink'>For You 💌</p>", unsafe_allow_html=True)

cols = st.columns(5)
cols[0].image('images/pajama2.jpg')
cols[1].image('images/pajama3.jpg')
cols[2].image('images/pajama4.jpg')
cols[3].image('images/pajama5.jpg')
cols[4].image('images/pajama.jpg')

cols = st.columns(5)
cols[0].image('images/pajama2.jpg')
cols[1].image('images/pajama3.jpg')
cols[2].image('images/pajama4.jpg')
cols[3].image('images/pajama5.jpg')
cols[4].image('images/pajama.jpg')

cols = st.columns(5)
cols[0].image('images/pajama2.jpg')
cols[1].image('images/pajama3.jpg')
cols[2].image('images/pajama4.jpg')
cols[3].image('images/pajama5.jpg')
cols[4].image('images/pajama.jpg')

cols = st.columns(5)
cols[0].image('images/pajama2.jpg')
cols[1].image('images/pajama3.jpg')
cols[2].image('images/pajama4.jpg')
cols[3].image('images/pajama5.jpg')
cols[4].image('images/pajama.jpg')

