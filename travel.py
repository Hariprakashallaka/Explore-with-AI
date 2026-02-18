import streamlit as st
from google import genai

# ===============================
# CONFIGURATION
# ===============================

API_KEY = "AIzaSyA-VULUOb4-itYPmjzPxyONpbX2xA0KZZA"
MODEL_NAME = "gemini-2.0-flash"

client = genai.Client(api_key=API_KEY)


# ===============================
# AI GENERATION FUNCTION
# ===============================
def generate_itinerary(destination, days, nights, budget, interests):

    prompt = f"""
You are an expert AI travel planner.

Create a highly detailed, realistic, and NON-REPETITIVE travel itinerary.

Trip Details:
Destination: {destination}
Duration: {days} Days and {nights} Nights
Budget: {budget}
User Interests: {', '.join(interests)}

STRICT RULES:
- Generate EXACTLY {days} days.
- Each day must be COMPLETELY DIFFERENT.
- Do NOT repeat the same attractions.
- Do NOT repeat similar wording.
- Rotate themes across days (culture, adventure, food, relaxation, shopping, nature, local life).
- Include specific place examples (realistic but general).
- Adjust activities based on budget level.
- Strongly focus on selected interests.
- Keep content practical and realistic.
- Use proper markdown formatting.

FORMAT:

## {destination} {days} Days & {nights} Nights Itinerary

Write a short engaging introduction paragraph.

Then for each day:

**Day 1 – Theme of the Day**
**Morning:** Detailed activity  
**Afternoon:** Detailed activity  
**Evening:** Detailed activity  

Continue this structure until Day {days}.
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return response.text

    except Exception:
        # Improved dynamic fallback with variation
        fallback = f"""
## {destination} {days} Days & {nights} Nights Itinerary

This personalized itinerary focuses on {', '.join(interests)} experiences under a {budget} budget.
"""

        themes = [
            "Cultural Exploration",
            "Adventure & Outdoor",
            "Local Cuisine Discovery",
            "Historical Landmarks",
            "Nature & Scenic Views",
            "Shopping & Local Markets",
            "Relaxation & Leisure"
        ]

        for i in range(1, days + 1):
            theme = themes[(i - 1) % len(themes)]

            fallback += f"""

**Day {i} – {theme}**
**Morning:** Start your day with a {theme.lower()} experience exploring a key attraction in {destination}.
**Afternoon:** Continue with engaging activities related to {theme.lower()} while enjoying local atmosphere.
**Evening:** Wind down with a unique evening experience aligned with {theme.lower()}.
"""

        return fallback



# ===============================
# STREAMLIT UI
# ===============================

def main():

    st.set_page_config(page_title="Explore with AI", layout="centered")

    st.title("🌍 Explore with AI: Custom Itineraries for Your Next Journey")

    st.write("Generate intelligent and personalized travel plans using AI.")

    # USER INPUTS
    destination = st.text_input("Enter Destination")

    days = st.number_input("Number of Days", min_value=1, step=1)
    nights = st.number_input("Number of Nights", min_value=0, step=1)

    budget = st.selectbox(
        "Select Budget Preference",
        ["Economy", "Standard", "Luxury"]
    )

    interests = st.multiselect(
        "Select Travel Interests",
        ["Adventure", "Spiritual", "Food", "Nature", "Historical", "Shopping"]
    )

    # BUTTON
    if st.button("Generate Itinerary"):

        if destination.strip() == "":
            st.error("Please enter a destination.")
            return

        if not interests:
            st.error("Please select at least one interest.")
            return

        with st.spinner("Generating Personalized Itinerary..."):

            itinerary = generate_itinerary(
                destination,
                days,
                nights,
                budget,
                interests
            )

        st.success("Generated Itinerary")

        st.markdown(itinerary)

        # DOWNLOAD OPTION
        st.download_button(
            label="Download Itinerary",
            data=itinerary,
            file_name=f"{destination}_itinerary.txt",
            mime="text/plain"
        )


# ===============================
# RUN APP
# ===============================

if __name__ == "__main__":
    main()
