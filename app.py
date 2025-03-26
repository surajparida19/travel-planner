# import streamlit as st
# import google.generativeai as genai
# import re  # Import the regular expression module

# # Set up Gemini API key

# genai.configure(api_key=GEMINI_API_KEY)

import streamlit as st
import google.generativeai as genai
import re  # Import the regular expression module

# Set up Gemini API key
GEMINI_API_KEY = "AIzaSyBvLxH_CL8nm17Ake-Cr0KMdC8FFYoKmiU"  # Replace with your actual API key
genai.configure(api_key=GEMINI_API_KEY)

# Function to remove Markdown
def remove_markdown(text):
    """Removes Markdown bold (**) and other formatting from text."""
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # Remove bold
    text = re.sub(r'\*(.*?)\*', r'\1', text)      # Remove italics
    text = re.sub(r'_([^_]*)_', r'\1', text)        # Remove underscores for italics
    return text

# Background image URL
background_url = "https://raw.githubusercontent.com/surajparida19/travel-planner/main/Background.jpg"

# CSS Styles
css = f"""
<style>
    .main {{
        background-image: url("{background_url}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        height: 100vh;
        padding: 20px;
    }}

    .stButton>button {{
        background-color: #28a745;
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        transition: 0.3s;
    }}

    .stButton>button:hover {{
        background-color: #218838;
    }}

    .stTextInput>div>input {{
        border-radius: 8px;
        padding: 10px;
        border: 1px solid #ccc;
    }}

    .stTextArea>div>textarea {{
        border-radius: 8px;
        padding: 10px;
        border: 1px solid #ccc;
    }}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# App Title
st.title("\u2708\ufe0f AI Travel Planner")

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
        model = genai.GenerativeModel("models/gemini-1.5-flash-001")

        response = model.generate_content(prompt)

        # Display itinerary after removing markdown.
        if response.text:
            cleaned_text = remove_markdown(response.text)
            st.text_area("Your Travel Itinerary:", cleaned_text, height=400)
        else:
            st.error("Failed to generate itinerary. Please try again.")

    else:
        st.error("Please fill in all required details.")
)
