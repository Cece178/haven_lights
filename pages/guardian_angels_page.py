import streamlit as st


st.markdown("<h1 style='text-align: center; margin-bottom: 0.001em'>Your Guardian Angels</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Meet your angels!</h2>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; margin-bottom: 0.01em'>Your primary angels are marked with a 💖</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; margin-top: 0.01em'>All other angels are 🪽</p>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        text-align:center;
        width:100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

#start of Gemini code
st.markdown(
    """
    <style>
    .button-container {
        background-image: url("main_app/images/gradient_pink.jpg") !important;
        background-size: cover !important;
        background-repeat: no-repeat !important;
        padding: 20px !important;
    }
    .stButton > button:first-child {
        text-align:center;
        width:100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
#end of Gemini code

with st.container(): #start of Gemini code
    st.markdown('<div class="button-container">', unsafe_allow_html=True) #end of Gemini code
    st.button("Selene💖 ––→  3km away")
    st.button("Dad💖 ––→  5km away")
    st.button("Mom💖 ––→  10km away")
    st.button("Leah🪽 ––→  2km away")
    st.button(" Add another angel☁️")
    st.markdown('</div>', unsafe_allow_html=True) #line of Gemini code

st.page_link(page="pages/map_page.py", label="Map")