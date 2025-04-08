#code by Gemini
import streamlit as st
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim

#my code
st.markdown("<h1 style= 'text-align: center; margin-bottom: 0.01em'>🗺️   Map   🗺️</h1>", unsafe_allow_html=True)
st.markdown("<p style= 'text-align: center; color: pink; margin-bottom: 2em'>Your safe spots will be displayed like this:☁️</p>", unsafe_allow_html=True)
#end of my code

#Gemini Code
# Default Location (Queenstown, New Zealand)
default_latitude = -45.031162
default_longitude = 168.662643

# Initialize the geolocator
geolocator = Nominatim(user_agent="haven_lights_app")  # Replace with your app name

# Initialize a list to store pinned locations
if "pinned_locations" not in st.session_state:
    st.session_state.pinned_locations = []

# Create a Folium map
m = folium.Map(location=[default_latitude, default_longitude], zoom_start=12)

# Add a marker for the default location with a custom icon
folium.Marker(
    [default_latitude, default_longitude],
    popup="Queenstown",
    icon=folium.Icon(color="red", icon="info-sign"),  # Customize the icon here
).add_to(m)

# Address Input
address = st.text_input("Enter Address of Your Safe Spot!", placeholder="Safe spot address goes here...", key="address")

if address:
    try:
        # Geocode the address
        location = geolocator.geocode(address)
        if location:
            latitude = location.latitude
            longitude = location.longitude

            # Add the new location to the session state
            st.session_state.pinned_locations.append({"address": address, "latitude": latitude, "longitude": longitude})

            # Add a marker for the entered address with a custom icon
            folium.Marker(
                [latitude, longitude],
                popup=address,
                icon=folium.Icon(color="pink", icon="cloud"),  # Customize the icon here
            ).add_to(m)

            # Center the map on the new location
            m.location = [latitude, longitude]
            m.zoom_start = 12  # Adjust zoom level as needed
        else:
            st.error("Could not geocode the address. Please enter a valid address.")

    except Exception as e:
        st.error(f"Error: {e}")

# Display the map in Streamlit
folium_static(m)

# Display pinned locations as labels
st.subheader("Pinned Locations")
for pinned_location in st.session_state.pinned_locations:
    st.write(pinned_location["address"])
