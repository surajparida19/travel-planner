
# ✈️ AI Travel Planner

A simple and interactive AI-powered travel itinerary generator built using **Streamlit** and **Google Gemini API**. Just enter your trip details — starting location, destination, number of days, budget, and purpose — and let AI craft a personalized travel plan for you!

---

## 🚀 Features

- 🌍 Generate day-wise travel itineraries
- 💸 Budget-based recommendations (Low, Medium, High)
- 🎯 Customize trips for different purposes (Adventure, Relaxation, Work, Honeymoon, etc.)
- 🍽️ Suggests places to visit, food options, and travel tips
- 🤖 Powered by **Google Gemini 1.5 Flash Model**
- 🧠 Uses generative AI to create unique plans every time

---

## 📸 Preview

![AI Travel Planner Preview](https://via.placeholder.com/800x400?text=App+Preview)  
*Replace with a real screenshot after running your app*

---

## 🛠️ Tech Stack

- Python
- [Streamlit](https://streamlit.io/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)

---

## 🧑‍💻 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-travel-planner.git
cd ai-travel-planner
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> `requirements.txt` should contain:
> ```
> streamlit
> google-generativeai
> ```

### 3. Set Your Google Gemini API Key

You can export your API key as an environment variable or place it directly in the script (not recommended for production).

```bash
export GEMINI_API_KEY="your-api-key-here"
```

Or replace directly in the script:
```python
GEMINI_API_KEY = "your-api-key-here"
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
ai-travel-planner/
├── app.py
├── requirements.txt
└── README.md
```

---

## 🔐 Security Note

⚠️ **Never share or upload your real API key to public repositories.** Use `.env` files or environment variables to protect sensitive information.

---

## 🌟 Future Improvements

- Add map visualizations and weather integration
- Allow downloading the itinerary as PDF
- Support for multi-city trip planning
- User login and saved trips

---

## 📬 Contact

Made with ❤️ by [Your Name](https://github.com/your-username)  
📧 Reach me at: your-email@example.com

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).
