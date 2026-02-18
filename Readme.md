# 🌍 AI-Powered Travel Itinerary Generator

An intelligent web-based travel planning application that generates personalized multi-day travel itineraries using Google Gemini (Generative AI).

---

## 🚀 Project Overview

This application allows users to generate customized travel itineraries based on:

- Destination
- Number of Days & Nights
- Budget Preference (Economy / Standard / Luxury)
- Travel Interests (Adventure, Food, Nature, Historical, etc.)

The system dynamically generates an itinerary for the exact number of days entered by the user using prompt engineering techniques.

---

## 🛠 Tech Stack

- **Programming Language:** Python
- **Frontend Framework:** Streamlit
- **AI Integration:** Google Gemini API (Generative AI)
- **Deployment:** Streamlit Community Cloud
- **Version Control:** GitHub

---

## ✨ Key Features

- 🔹 Dynamic multi-day itinerary generation
- 🔹 Budget-based personalization
- 🔹 Interest-based activity customization
- 🔹 Non-repetitive day-wise planning
- 🔹 Download itinerary as text file
- 🔹 Error handling & fallback mechanism
- 🔹 Secure API key management using environment variables

---

## 📌 How It Works

1. User enters trip details.
2. Application sends a structured prompt to Gemini API.
3. AI generates a detailed itinerary.
4. Output is displayed in formatted markdown.
5. User can download the itinerary.

---

## 🔧 Installation (Run Locally)

1. Clone the repository:
```
git clone https://github.com/your-username/your-repo-name.git
```

2. Navigate into the project folder:
```
cd your-repo-name
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Set your Gemini API key as environment variable:
```
export GEMINI_API_KEY=your_api_key_here
```

5. Run the application:
```
streamlit run travel.py
```

---

## 🌐 Deployment

The application can be deployed easily using **Streamlit Community Cloud** by connecting the GitHub repository.

---

## 🎯 Learning Outcomes

- Prompt Engineering for Generative AI
- API Integration using Python
- Building interactive web apps using Streamlit
- Secure environment variable handling
- Deploying AI applications to the web
