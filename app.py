import openai
import streamlit as st
from textwrap import dedent

# Set up the Streamlit app
st.title("AI Travel Planner ✈️")
st.caption("Plan your next adventure with AI Travel Planner by researching and planning a personalized itinerary on autopilot using GPT-4")

# Get OpenAI API key from user
openai_api_key = st.text_input("Enter OpenAI API Key to access GPT-4", type="password")

# Define the function to call the OpenAI API
def call_openai(prompt, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Specify the correct model name here
        messages=[
            {"role": "system", "content": "You are a world-class travel planner."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500,
        temperature=0.7,
    )
    return response.choices[0].message['content'].strip()

if openai_api_key:
    # Input fields for the user's destination and the number of days they want to travel for
    destination = st.text_input("Where do you want to go?")
    num_days = st.number_input("How many days do you want to travel for?", min_value=1, max_value=30, value=7)

    if st.button("Generate Itinerary"):
        with st.spinner("Processing..."):
            # Create prompt for the OpenAI API
            prompt = dedent(f"""
            Given a travel destination and the number of days the user wants to travel for,
            generate a detailed itinerary including the best travel destinations, activities, and accommodations.

            Destination: {destination}
            Number of days: {num_days}

            Please provide a detailed itinerary.
            """)
            # Get the response from the OpenAI API
            response = call_openai(prompt, openai_api_key)
            st.write(response)
