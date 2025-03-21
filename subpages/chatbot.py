import openai
import streamlit as st
import pandas as pd
import json

# Load OpenAI API key
client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

# Load dataset
df = pd.read_csv("./air_pollution_data.csv")  # Adjust dataset path

# Function to compute key statistics
def get_dataset_summary():
    summary = {

        "Average AQI per City": df.groupby("city")["aqi"].mean().to_dict(),
        "Average AQI per Year": df.groupby(df["date"].str[:4])["aqi"].mean().to_dict(),
        "Pollutant Averages per City": df.groupby("city").mean(numeric_only=True).to_dict(),
        "Pollutant Averages per Year": df.groupby(df["date"].str[:4]).mean(numeric_only=True).to_dict(),
    }
    return summary

# Function to summarize columns efficiently
def get_columns_summary():
    summary = {}

    # Numeric column statistics
    numeric_summary = df.describe().to_dict()

    
    summary["Numeric Columns Summary"] = numeric_summary
    

    return summary

# Function to get a small random subset of the dataset
def get_sample_data(n=3):
    return df.sample(n=n, random_state=42).to_json(orient="records")

# Function to split large text into chunks (ensuring token limit)
def chunk_text(text, max_tokens=4000):
    words = text.split()
    chunks = []
    while words:
        chunk = " ".join(words[:max_tokens])
        chunks.append(chunk)
        words = words[max_tokens:]
    return chunks

# Function to send all chunks sequentially
def query_openai(question):
    try:
        dataset_summary = json.dumps(get_dataset_summary(), indent=2)  # Convert to JSON string
        sample_data = get_sample_data()
        columns_summary = json.dumps(get_columns_summary(), indent=2)  # Convert to JSON

        full_prompt = f"""
        You are an AI assistant analyzing air pollution data. Below are the dataset details:

        **Dataset Summary**:
        {dataset_summary}
        
        **Sample Data**:
        {sample_data}

        **All Columns Summary**:
        {columns_summary}

        Once you have all context, I will ask my question.
        """

        # Chunk the prompt into smaller parts
        chunks = chunk_text(full_prompt, max_tokens=4000)

        messages = [{"role": "system", "content": "You are an expert in air pollution analysis."}]

        # Send chunks iteratively to OpenAI, maintaining conversation context
        for chunk in chunks:
            messages.append({"role": "user", "content": chunk})
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.5
            )
            messages.append({"role": "assistant", "content": response.choices[0].message.content})

        # Finally, ask the user’s question
        messages.append({"role": "user", "content": f"Now answer this question: {question}"})
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.5
        )

        return response.choices[0].message.content
    except openai.OpenAIError as e:  #  Correct OpenAI error handling
        st.error(" Something went wrong while communicating with OpenAI. Please try again.")
        return " Unable to process your request at the moment."

    except Exception as e:  
        st.error("An unexpected error occurred. Please try again later.")
        return " Something went wrong. Please try again."

# Streamlit UI
def show_chatbot():
    st.title("AI Chatbot for Air Quality Data")

    user_input = st.text_input("Ask a question about the dataset:")
    if st.button("Get Answer"):
        if user_input:
            answer = query_openai(user_input)
            st.write(answer)
        else:
            st.warning("Please enter a question.")
