import streamlit as st

def show_dashboard_page():
    st.title(" Air Quality Index Dashboard")
    
    st.subheader("city specific:")
    st.components.v1.html(
            f"<iframe title='pollutant details with cities' width='100%' height='400px' "
            f"src='{st.session_state['config']['page1']}' frameborder='0' allowFullScreen='true'></iframe>", 
            height=450
        )
    st.write("This interactive map visualizes the AQI levels of 26 cities, offering a geographic perspective on air quality variations. Each city is marked, allowing you to identify pollution hotspots and cleaner areas easily.")

    st.write("### City-Specific AQI Trends")
    st.write("Select a city from the dropdown to explore its historical AQI trends through the graph. Gain quick insights into:")
    st.write("- Average PM2.5 levels")
    st.write("- Average AQI value")
    st.write("- Average PM10 levels")
    st.write("- Average CO levels")
    st.write("- Average NO2 levels")

    st.components.v1.html(
            f"<iframe title='pollutant details with cities' width='100%' height='400px' "
            f"src='{st.session_state['config']['page2']}' frameborder='0' allowFullScreen='true'></iframe>", 
            height=450
        )
    st.write("### Air Quality Dashboard")  
    st.write("This dashboard provides insights into pollution trends across 26 cities. It includes:")  
    st.write("- **Pollutant Trends Over the Years**: Visualizing how pollutant levels have changed annually.")  
    st.write("- **City-Wise Pollution Levels**: Comparing pollutant concentrations across different cities.")  
    st.write("- **Worst & Best Cities**: Highlighting the four cities with the highest and lowest AQI levels.")  

    st.components.v1.html(
            f"<iframe title='pollutant details with cities' width='100%' height='400px' "
            f"src='{st.session_state['config']['page3']}' frameborder='0' allowFullScreen='true'></iframe>", 
            height=450
        )
    st.title("Traffic Impact on Air Quality ")

    # Description
    st.markdown("""
    ## **Understanding the Relationship Between Traffic and Air Quality**
    This visualization explores how **traffic-related pollutants** impact overall air quality across cities.

    ### **Graph 1: NO₂ vs AQI**
    - **X-Axis:** Nitrogen Dioxide (NO₂) levels  
    - **Y-Axis:** Air Quality Index (AQI)  
    - **Insight:** Since NO₂ is a key emission from vehicles, an upward trend in AQI with rising NO₂ levels may indicate that **traffic congestion contributes to poor air quality**.

    ### **Graph 2: CO vs AQI**
    - **X-Axis:** Carbon Monoxide (CO) levels  
    - **Y-Axis:** Air Quality Index (AQI)  
    - **Insight:** CO is another traffic-related pollutant. If AQI increases with CO levels, it suggests **vehicular emissions significantly impact air pollution**.

    ### **Key Takeaways**
     Helps assess how vehicle emissions impact overall air quality.  
    Identifies whether **stricter traffic control measures** could improve air conditions.  
     Supports decision-making for **urban planning and pollution control policies**.

    **This analysis enables us to better understand and mitigate the effects of traffic on air pollution!** 🚗💨
    """)
    st.title("Seasonal Trends in Air Quality Index (AQI)")

    # Description
    st.markdown("""
    ## How Seasons Impact Air Quality
    This visualization examines how AQI varies across different seasons, helping to identify trends in air pollution.

    ### Graph Overview
    - **X-Axis:** Seasons (Winter, Spring, Summer, Autumn)  
    - **Y-Axis:** Average Air Quality Index (AQI)  
    - **Insight:** The variation in AQI across seasons helps identify periods of high and low pollution levels.

    ### Seasonal Trends
    - **Winter:** Often the worst season for air quality due to temperature inversion trapping pollutants.  
    - **Spring:** Moderate air quality as weather transitions.  
    - **Summer:** Generally better air quality due to higher wind speeds dispersing pollutants.    
    - **Autumn:** Pollution levels start rising due to post-monsoon temperature drops and crop burning in some regions.  

    ### Key Takeaways
    - Helps predict seasonal air pollution levels.  
    - Identifies when air quality worsens, allowing for preventive measures.  
    - Supports government policies on pollution control for high-risk seasons.  

    This analysis provides useful insights into how AQI fluctuates throughout the year.  
    """)

    st.components.v1.html(
            f"<iframe title='pollutant details with cities' width='100%' height='400px' "
            f"src='{st.session_state['config']['page4']}' frameborder='0' allowFullScreen='true'></iframe>", 
            height=450
        )
    st.write("This visualization predicts the Air Quality Index (AQI) for the next five years based on historical data . The forecast helps in understanding long-term air pollution patterns, enabling better planning for environmental and public health initiatives")

    