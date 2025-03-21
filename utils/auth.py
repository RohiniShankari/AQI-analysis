import streamlit as st

def authenticate_user(username, password):
    """Authenticate user from session state"""
    return username in st.session_state["users"] and st.session_state["users"][username] == password

def create_user(username, password):
    """Create a new user"""
    if username in st.session_state["users"]:
        return False  # Username already exists
    st.session_state["users"][username] = password
    return True
