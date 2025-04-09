import streamlit as st

st.markdown("<h1 style='text-align: center;'>🥸 Profile 🥸</h1>", unsafe_allow_html=True)

name = st.text_input("Name", placeholder="Enter your name", key="name")
email = st.text_input("Email", placeholder="Enter your email", key="email")
phone_number = st.text_input("Phone Number", placeholder="Enter your phone number", key="phone_number")

if st.button("Save"):
    st.write(f"Name: {name}")
    st.write(f"Email: {email}")
    st.write(f"Phone Number: {phone_number}")
    st.toast("Information saved!", icon="🥸")
