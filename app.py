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
# List of cities and states
cities_states = [
    "New York City, NY", "Los Angeles, CA", "Chicago, IL", "Houston, TX",
    "Phoenix, AZ", "Philadelphia, PA", "San Antonio, TX", "San Diego, CA",
    "Dallas, TX", "San Jose, CA", "Austin, TX", "Seattle, WA",
    "Denver, CO", "Washington, DC", "Boston, MA", "Miami, FL",
    "Atlanta, GA", "Nashville, TN", "New Orleans, LA", "India, Delhi",
    "India, Mumbai", "India, Bangalore", "India, Chennai", "India, Kolkata",
    "India, Hyderabad", "India, Pune", "India, Jaipur", "India, Lucknow",
    "India, Ahmedabad", "United Kingdom, London", "United Kingdom, Manchester",
    "United Kingdom, Birmingham", "United Kingdom, Liverpool", "France, Paris",
    "France, Marseille", "France, Lyon", "Germany, Berlin", "Germany, Munich"
]

# Function to filter suggestions
def filter_suggestions(input_text, suggestions_list):
    if not input_text:
        return []
    input_text = input_text.lower()
    return [item for item in suggestions_list if input_text in item.lower()]

# CSS Styles
css = """
<style>
:root {
    --primary-color: #007bff;
    --secondary-color: #28a745;
    --background-color: #f5f5f5;
    --text-color: #333;
    --accent-color: #ffc107;
}

body {
    font-family: Arial, sans-serif;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
    background-color: var(--background-color);
    color: var(--text-color);
    max-width: 800px;
    line-height: 1.6;
    background-image: url("https://github.com/surajparida19/travel-planner/blob/main/Background.jpg"); /* Replace with your image path */
    background-size: cover; /* Cover the entire viewport */
    background-repeat: no-repeat; /* Prevent image repetition */
    background-attachment: fixed; /* Fixed background */
    color: white; /* Adjust text color for readability */
}

#itinerary {
    background-color: rgba(255, 255, 255, 0.8)
    background-color: #f5f5f5; /* Light background */
    color: #333; /* Darker text for readability */
}

button {
    transition: background-color 0.3s ease, transform 0.2s ease; /* Added transition */
}

button:hover {
    transform: translateY(-2px); /* Slight lift on hover */
}

#itinerary {
    background-color: white;
}

header {
    background: var(--primary-color);
    color: white;
    padding: 15px;
}

h1 {
    margin: 0;
    font-weight: bold;
    font-size: 2em;
}

input, select, textarea {
    width: 95%;
    padding: 10px;
    margin: 5px 0 15px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}

textarea {
    resize: vertical;
}

#itinerary {
    padding: 20px;
    text-align: left;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin-top: 20px;
}

#itinerary ul {
    list-style-type: none;
    padding: 0;
}

#itinerary li {
    margin-bottom: 10px;
    padding-left: 20px;
    position: relative;
}

#itinerary li::before {
    content: "•";
    position: absolute;
    left: 0;
}

button {
    padding: 12px 20px;
    background: var(--secondary-color);
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 5px;
    transition: background-color 0.3s ease;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    margin-top: 5px;
}

button:hover {
    background-color: #218838;
}

.suggestion-button {
    background-color: #e0e0e0;
    color: #333;
    border: none;
    padding: 8px 12px;
    margin: 2px;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.suggestion-button:hover {
    background-color: #d0d0d0;
}

@media (max-width: 600px) {
    body {
        padding: 10px;
    }
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

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
