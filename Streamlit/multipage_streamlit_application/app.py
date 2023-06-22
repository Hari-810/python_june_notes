import streamlit as st
from pages import home, about, contact

# Set page title and configure layout
st.set_page_config(page_title="Multi-Page App", layout="wide")

# Create a dictionary to map page names to their respective functions
pages = {
    "Home": home,
    "About": about,
    "Contact": contact
}

# Sidebar navigation
page_selection = st.sidebar.radio("Navigate", tuple(pages.keys()))

# Display the selected page content
pages[page_selection]()
