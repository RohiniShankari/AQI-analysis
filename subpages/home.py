import streamlit as st

def show_home_page():
    st.title(" Air Quality Analysis")
    st.write(f"Welcome, **{st.session_state['username']}**! ")
    #st.write("Explore the air quality trends across 26 cities over the past four years with interactive visualizations. This dashboard provides  insights into air pollution levels, seasonal trends, and the impact of different pollutants on the Air Quality Index (AQI).")
    st.markdown("""
         
        This platform provides a data-driven analysis of pollution levels, emissions, and future AQI trends.  
        Explore the air quality trends across 26 cities over the past four years with interactive visualizations. This dashboard provides  insights into air pollution levels, seasonal trends, and the impact of different pollutants on the Air Quality Index (AQI).
        ###  **What You Can Explore**  
        - **City Emissions**: Check gas levels in different cities  
        -  **Pollution Trends**: Analyze gas concentration over time  
        -  **Traffic & Seasons**: Understand how AQI changes with seasons and traffic  
        -  **AQI Forecast**: View predicted AQI levels for the next 5 years  
        -  **feedback**:please share your through the feedback
        -  **chatbot**:ask any dataset related querys in the chatbot
        -  **quick test**:take the quiz to test your knowledge on this topic
        Use the sidebar to navigate through different sections!
    """)
 