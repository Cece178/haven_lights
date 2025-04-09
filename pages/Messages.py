#my code
import streamlit as st

st.markdown("<h1 style='text-align: center;'>💬 Talk To Your Angels 💬</h1>", unsafe_allow_html=True) 

with st.container():
    st.markdown('<div class="button-container">', unsafe_allow_html=True) 
    if st.button("Selene💖", use_container_width=True):
        st.markdown("<h6 style='text-align: left; color: white'>Hey girl! Where should we meet?</span>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: right;'>How about the mall?</h6>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: left; color: white'>Perfect! Would you mind turining your phone off silent? I'm going to be walking from home to the mall, so I might need you if something happens!</h6>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: right;'>Of course, I've got you! Thank goodness we found Haven, right?💗</h6>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: left; color: white'>Totally!</h6>", unsafe_allow_html=True)
        st.chat_input("Texting feature is coming soon, here is what it would look like!", key="chat_input")
        
    if st.button("Dad💖", use_container_width=True):
        st.markdown("<h6 style='text-align: left; color: white'>Ari, please let us know when the movie ends! I can pick you up if you need me to.</span>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: right;'>Thanks Dad, but I'll be okay! Selene and I will take the bus home. No need to worry 🥰</h6>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: left; color: white'>You know I'll always worry... Keep your phone handy in case you need to use your panic button!</h6>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: right;'>I will, I promise!</h6>", unsafe_allow_html=True)
        st.chat_input("Texting feature is coming soon, here is what it would look like!", key="chat_input")

    if st.button("Mom💖", use_container_width=True):
        st.markdown("<h6 style='text-align: right;'>Hey mom, just to let you know I should be home around 8pm. I'll let you know if anything changes, though.😘</h6>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: left; color: white'>Okay, darling, thank you! Be safe. Is your phone charged?</h6>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: right;'>It's at 86%!</h6>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: left; color: white'>Okay. Have fun, darling!</h6>", unsafe_allow_html=True)
        st.chat_input("Texting feature is coming soon, here is what it would look like!", key="chat_input")

    if st.button("Leah🪽", use_container_width=True):
        st.markdown("<h6 style='text-align: right;'>Hey sis, did you make it to the library alright?</h6>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: left; color: white'>Yes, I did!</h6>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: right;'>Were you scared to go somewhere by yourself?</h6>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: left; color: white'>A little bit, but I practiced my self defence moves with momma and she showed me how to use the panic button if I needed it😘🤪😎</h6>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: right;'>That's great! Have fun at the library and call if you need me 🥰🤪😎</h6>", unsafe_allow_html=True)
        st.chat_input("Texting feature is coming soon, here is what it would look like!", key="chat_input")
    st.markdown('</div>', unsafe_allow_html=True) 


