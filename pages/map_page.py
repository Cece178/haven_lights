import streamlit as st
import streamlit.components.v1 as components  # For embedding HTML/JavaScript
from streamlit_extras.switch_page_button import switch_page  # For navigation
from PIL import Image  # For image handling

st.title ("Map Page")
st.write("This is the map page.")  


def map_page():
    """Creates the map page with title, icons, map, and bottom navigation."""

    # Load icons as images (make sure these files are in the same directory or adjust paths)
    coin_icon = Image.open("coin_icon.png")  # Replace with your coin icon image
    messages_icon = Image.open("messages_icon.png") # Replace with your messages icon image
    home_icon = Image.open("home_icon.png") # Replace with your home icon image
    wings_icon = Image.open("wings_icon.png") # Replace with your wings icon image
    exclamation_icon = Image.open("exclamation_icon.png") # Replace with your exclamation icon image
    map_icon = Image.open("map_icon.png") # Replace with your map icon image
    person_icon = Image.open("person_icon.png") # Replace with your person icon image

    # Center the title and add icons to the sides
    col1, col2, col3 = st.columns([1, 4, 1])  # Create columns for layout
    with col1:
        if st.button(coin_icon):
            st.write("Coin button clicked!") #placeholder action
    with col2:
        st.markdown(
            "<h1 style='text-align: center; font-family: Broadway;'>Map</h1>",
            unsafe_allow_html=True,
        )  # Center the title using HTML and CSS
    with col3:
        if st.button(messages_icon):
            st.write("Messages button clicked!") #placeholder action

    # Embed a simple map (you can replace this with a more advanced map)
    st.map() # This is the basic streamlit map. You can add points, lines, etc.

    # Bottom navigation row
    col1, col2, col3, col4, col5 = st.columns(5) # Create 5 columns for the bottom icons
    with col1:
        if st.button(home_icon):
            switch_page("home") # switch to home.py
    with col2:
        if st.button(wings_icon):
            switch_page("guardian_angels") # switch to guardian_angels.py
    with col3:
        if st.button(exclamation_icon):
            st.write("Exclamation button clicked!") #placeholder action
    with col4:
        if st.button(map_icon):
            st.write("Map button clicked!") #placeholder action
    with col5:
        if st.button(person_icon):
            st.write("Person button clicked!") #placeholder action
if __name__ == "__main__":
    map_page()