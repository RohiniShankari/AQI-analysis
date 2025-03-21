import streamlit as st
from streamlit_option_menu import option_menu

from subpages import home, login, sections, settings, feedback,chatbot,quiz,dashboard
from utils.config import CONFIG


st.set_page_config(page_title="AQI Analysis")
# ---- Initialize Session State ----
if "users" not in st.session_state:
    st.session_state["users"] = {"admin": "admin123"}
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""
if "page" not in st.session_state:
    st.session_state["page"] = "Login"
if "config" not in st.session_state:
    st.session_state["config"] = CONFIG  # Importing from config.py

# ---- Sidebar Navigation ----
if st.session_state["logged_in"]:
    with st.sidebar:
        selected_menu = option_menu(
            menu_title="AQI analysis",
            options=["Home","Dashboard", "city specific", "AirMetrics", "Aqi patterns", "AQI forecast", "quick test","chatbot", "Feedback", "Settings", "Logout"],
            icons = ["house", "bar-chart","geo-alt", "graph-up", "activity","cloud-sun", "book","robot",  "chat-dots", "gear", "box-arrow-right"],
            menu_icon="blank",
            default_index=0
        )
        
        if selected_menu == "Logout":
            st.session_state["logged_in"] = False
            st.session_state["username"] = ""
            st.session_state["page"] = "Login"
            st.rerun()
        else:
            st.session_state["page"] = selected_menu

# ---- Page Routing ----
if st.session_state["page"] == "Login":
    login.show_login_page()
elif st.session_state["page"]=="Signup":
    login.show_signup_page()
elif st.session_state["page"] == "Home":
    home.show_home_page()
elif st.session_state["page"]=="Dashboard":
    dashboard.show_dashboard_page()
elif st.session_state["page"] == "city specific":
    sections.show_section1()
elif st.session_state["page"] == "AirMetrics":
    sections.show_section2()
elif st.session_state["page"] == "Aqi patterns":
    sections.show_section3()
elif st.session_state["page"] == "AQI forecast":
    sections.show_section4()
elif st.session_state["page"] == "quick test":
    quiz.show_quiz()
elif st.session_state["page"]=="chatbot":
    chatbot.show_chatbot()
elif st.session_state["page"] == "Feedback":
    feedback.show_feedback_page()
elif st.session_state["page"] == "Settings":
    settings.show_settings_page()
