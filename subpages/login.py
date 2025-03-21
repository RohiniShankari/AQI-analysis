import streamlit as st
from utils.auth import authenticate_user, create_user

def show_login_page():
    st.title("Login ")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate_user(username, password):
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["page"] = "Home"
            st.rerun()
        else:
            st.error("Invalid username or password!")

    st.button("Go to Signup", on_click=lambda: st.session_state.update(page="Signup"))

def show_signup_page():
    st.title(" Signup ")

    new_username = st.text_input("Choose a Username")
    new_password = st.text_input("Choose a Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Signup"):
        if new_password != confirm_password:
            st.error(" Passwords do not match!")
        elif create_user(new_username, new_password):
            st.success("Account created! Please login.")
            st.session_state["page"] = "Login"
        else:
            st.error(" Username already exists!")

    st.button("Go to Login", on_click=lambda: st.session_state.update(page="Login"))
