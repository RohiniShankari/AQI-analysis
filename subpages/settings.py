import streamlit as st 

def show_settings_page():
    st.title("Settings")
    st.subheader("change username")
    # Change Username
    new_username = st.text_input("New Username", value=st.session_state["username"])
    if st.button("Update Username"):
        if new_username in st.session_state["users"]:
            st.error(" Username already exists!")
        else:
            st.session_state["users"][new_username] = st.session_state["users"].pop(st.session_state["username"])
            st.session_state["username"] = new_username
            st.success(" Username updated successfully!")

    # Change Password
    st.subheader("change password")
    new_password = st.text_input("New Password", type="password")
    confirm_password = st.text_input("Confirm New Password", type="password")
    if st.button("Update Password") and new_password == confirm_password:
        st.session_state["users"][st.session_state["username"]] = new_password
        st.success("Password updated successfully!")

    # Update Power BI Links
    st.subheader("change dashboard")
    for i in range(1, 5):
        st.session_state["config"][f"page{i}"] = st.text_input(f"Power BI Page {i} URL", st.session_state["config"][f"page{i}"])

    if st.button("Save Power BI Links"):
        st.success(" Power BI URLs updated successfully!")
