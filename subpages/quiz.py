import streamlit as st
def show_quiz():
    


    st.title(" Air Quality Quiz")
    st.write("Test your knowledge about air quality and pollution!")

    # Quiz Questions and Answers
    quiz_data = [
        {"question": "What does AQI stand for?", "options": ["Air Quality Index", "Air Quota Indicator", "Atmosphere Quality Impact"], "answer": "Air Quality Index"},
        {"question": "Which city has lowest AQI?", "options": ["Aizwal", "kochi", "delhi"], "answer": "Aizwal"},
        {"question": "Which city has highest AQI?", "options": ["Aizwal", "kochi", "delhi"], "answer": "delhi"},
        {"question": "Which year has highest average AQI?", "options": ["2020", "2021", "2022"], "answer": "2020"},
        {"question": "Which season has higest AQI?", "options": ["winter", "summer", "autumn"], "answer": "winter"},
        {"question": "Which season has lowest AQI?", "options": ["winter", "summer", "autumn"], "answer": "summer"},
        {"question": "Which of these health issues is linked to poor air quality?", "options": ["Lung diseases", "Hearing loss", "Hair loss"], "answer": "Lung diseases"},
        {"question": "Which year has lowest average AQI?", "options": ["2020", "2021", "2022"], "answer":"2022"},
        {"question": "what is average aqi of delhi?", "options": ["4.8", "4.5", "3.5"], "answer": "4.8"},
        {"question": "how can we reduce the air pullution?", "options": ["Using public transport", "Using more plastic", "Burning waste"], "answer": "Using public transport"}
    ]

    # Initialize session state
    if "selected_answers" not in st.session_state:
        st.session_state.selected_answers = [None] * len(quiz_data)
    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    # Function to handle answer selection
    def select_answer(question_index, selected_option):
        st.session_state.selected_answers[question_index] = selected_option

    # Function to submit quiz
    def submit_quiz():
        st.session_state.submitted = True
        st.session_state.score = sum(
            1 for i, q in enumerate(quiz_data) if st.session_state.selected_answers[i] == q["answer"]
        )

    # Display Quiz Questions
    for i, q in enumerate(quiz_data):
        st.subheader(f"Q{i+1}: {q['question']}")
        
        cols = st.columns(len(q["options"]))  # Create columns for buttons
        
        for j, option in enumerate(q["options"]):
            btn_color = "primary" if st.session_state.selected_answers[i] == option else "secondary"
            
            with cols[j]:  # Place buttons in respective columns
                if st.button(option, key=f"btn_{i}_{j}", use_container_width=True, type=btn_color):
                    select_answer(i, option)

    # Submit Button
    if st.button("Submit Quiz", key="submit_quiz", type="primary"):
        submit_quiz()

    # Show results after submission
    if st.session_state.submitted:
        st.subheader(f" Your Final Score: {st.session_state.score}/10")
        # Final message based on score
        if st.session_state.score > 7:
            st.success("Awesome! You know a lot about air quality! ")
        elif 4 <= st.session_state.score <= 7:
            st.warning("Not bad! A little more learning and you'll be an AQI expert! ")
        else:
            st.error("Keep learning! Air quality knowledge is important for a healthy life! ")

        for i, q in enumerate(quiz_data):
            if st.session_state.selected_answers[i] == q["answer"]:
                st.success(f" Q{i+1}: Correct!")
            else:
                st.error(f" Q{i+1}: Wrong! The correct answer is {q['answer']}.")

 