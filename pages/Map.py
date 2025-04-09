#code by Gemini
import streamlit as st
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim

#my code
st.markdown("<h1 style= 'text-align: center; margin-bottom: 0.01em'>🗺️   Map   🗺️</h1>", unsafe_allow_html=True)
st.markdown("<p style= 'text-align: center; color: pink; margin-bottom: 2em'>Your safe spots will be displayed like this:☁️</p>", unsafe_allow_html=True)
#end of my code

# Gemini Code
# Default Location
default_latitude = -45.031162
default_longitude = 168.662643

geolocator = Nominatim(user_agent="haven_app")  

if "pinned_locations" not in st.session_state:
    st.session_state.pinned_locations = []

if "map" not in st.session_state:
    st.session_state.map = folium.Map(location=[default_latitude, default_longitude], zoom_start=12)

    folium.Marker(
        [default_latitude, default_longitude],
        popup="Queenstown",
        icon=folium.Icon(color="red", icon="info-sign"),  
    ).add_to(st.session_state.map)

m = st.session_state.map

address = st.text_input("Enter Address of Your Safe Spot!", placeholder="Safe spot address goes here...", key="address")

if address:
    try:
        
        location = geolocator.geocode(address)
        if location:
            latitude = location.latitude
            longitude = location.longitude

            st.session_state.pinned_locations.append({"address": address, "latitude": latitude, "longitude": longitude})
            st.toast("Safe spot added!", icon="☁️")
            
            folium.Marker(
                [latitude, longitude],
                popup=address,
                icon=folium.Icon(color="pink", icon="cloud"), 
            ).add_to(m)

            m.location = [latitude, longitude]
            m.zoom_start = 12 
        else:
            st.error("Could not geocode the address. Please enter a valid address.")

    except Exception as e:
        st.error(f"Error: {e}")

folium_static(m)

st.subheader("Pinned Locations")
for pinned_location in st.session_state.pinned_locations:
    st.write(pinned_location["address"])