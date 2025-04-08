import streamlit as st

if st.button("🪙", type = 'tertiary'):
    st.switch_page("Home_app.py")

st.markdown("<h1 style='text-align: center;'>💤Haven Sleepwear💤</h1>", unsafe_allow_html=True)

st.markdown('<h4 style="text-align: center; color: pink">Sleep Like A Baby Collection</p>', unsafe_allow_html=True)



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


