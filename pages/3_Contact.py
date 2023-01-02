import streamlit as st

import requests

st.set_page_config(
    page_title="Skin Cancer",
    page_icon="♋",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Replace YOUR_API_KEY with your actual API key
api_key = "AIzaSyCfqty5e_JIBd-2RrdbB0W5ykv3D4noYNg"

# Set the location and radius for the search
location = "22.5726,88.3639"  # Your City
radius = 10000  # 10 km
keyword = "dermatologist"

# Make the request to the Places API
url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&keyword={keyword}&key={api_key}"
response = requests.get(url)
results = response.json()["results"]

# Extract the place IDs of the results
place_ids = [result["place_id"] for result in results]

# Use the place IDs to get the details of the places
dermatologists = []
for place_id in place_ids:
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={api_key}"
    response = requests.get(url)
    place_details = response.json()["result"]
    dermatologists.append(
        {
            "name": place_details["name"],
            "address": place_details["formatted_address"],
        }
    )

# Display the results in Streamlit
st.header("Nearby Dermatologists")
for dermatologist in dermatologists:
    st.markdown(f"**{dermatologist['name']}**")
    st.markdown(dermatologist["address"])
