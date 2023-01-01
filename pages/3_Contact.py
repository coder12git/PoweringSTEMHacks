import streamlit as st

city = st.text_input("City")

if st.button("Search"):
    if city != "":
        st.header("Results")
        st.map(data=None, zoom=10, use_container_width=True)
    else:
        st.error("Please enter a city")
