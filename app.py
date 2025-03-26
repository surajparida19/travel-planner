import streamlit as st
import google.generativeai as genai
import re  # Import the regular expression module

# Set up Gemini API key
GEMINI_API_KEY = "AIzaSyBvLxH_CL8nm17Ake-Cr0KMdC8FFYoKmiU"
genai.configure(api_key=GEMINI_API_KEY)

# Function to remove Markdown
def remove_markdown(text):
    """Removes Markdown bold (**) and other formatting from text."""
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # Remove bold
    text = re.sub(r'\*(.*?)\*', r'\1', text)      # Remove italics
    text = re.sub(r'_([^_]*)_', r'\1', text)      # Remove underscores for italics
    # Add other Markdown removal patterns as needed
    return text

# App Title
st.title("✈️ AI Travel Planner")

# User Inputs
start_location = st.text_input("Enter your starting location:")
destination = st.text_input("Enter your destination:")
trip_days = st.number_input("Number of days:", min_value=1, step=1)
budget = st.selectbox("Select your budget:", ["Low", "Medium", "High"])
trip_purpose = st.text_area("What is the purpose of your trip? (e.g., adventure, relaxation, work, honeymoon)")

# Generate Itinerary Button
if st.button("Generate Itinerary"):
    if destination and start_location and trip_days > 0:
        st.success("Generating your personalized itinerary...")

        # Create a prompt for Gemini
        prompt = f"""
        Create a detailed {trip_days}-day travel itinerary for a traveler going from {start_location} to {destination}. 
        The budget is {budget}, and the trip purpose is {trip_purpose}. 
        Include places to visit, food recommendations, and travel tips.
        """

        # Use the correct Gemini model
        model = genai.GenerativeModel("models/gemini-1.5-flash-001")  # Faster model
        # model = genai.GenerativeModel("models/gemini-2.0-pro-exp")  # More advanced model

        response = model.generate_content(prompt)

        # Display itinerary after removing markdown.
        if response.text:
            cleaned_text = remove_markdown(response.text)
            st.text_area("Your Travel Itinerary:", cleaned_text, height=400)
        else:
            st.error("Failed to generate itinerary. Please try again.")

    else:
        st.error("Please fill in all required details.")
