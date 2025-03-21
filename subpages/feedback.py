
import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load SMTP details
SMTP_SERVER = st.secrets["email"]["smtp_server"]
SMTP_PORT = st.secrets["email"]["smtp_port"]
SMTP_USER = st.secrets["email"]["smtp_user"]
SMTP_PASSWORD = st.secrets["email"]["smtp_password"]
SENDER_EMAIL = st.secrets["email"]["sender_email"]
RECEIVER_EMAILS = st.secrets["email"]["receiver_emails"]

def send_feedback( feedback):
    """Function to send feedback via email."""
    try:
        # Create email message
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = ", ".join(RECEIVER_EMAILS)
        msg["Subject"] = "New Feedback Submission"

        # Email content
        body = f"""
        New feedback received:
        
         
        Feedback: {feedback}
        """

        msg.attach(MIMEText(body, "plain"))

        # Send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAILS, msg.as_string())

        return True  # Email sent successfully
    except Exception as e:
        st.error(f"⚠️ Error sending feedback: {e}")
        #st.text(traceback.format_exc())  # Show full error traceback
        
        return False  # Email sending failed

def show_feedback_page():
    
    st.title("Share Your Thoughts")

    
    feedback = st.text_area("Your Feedback", placeholder="Enter your feedback here...")

    if st.button("Submit Feedback"):
        if  feedback:
            success = send_feedback(feedback)
            if success:
                st.success(" Thank you! Your feedback has been sent.")
            else:
                st.error("Failed to send feedback. Please try again later.")
        else:
            st.warning(" Please fill the feedback field before submitting.")
