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
You are a professional AI travel planner.

Create a personalized and detailed travel itinerary.

Destination: {destination}
Duration: {days} Days and {nights} Nights
Budget Type: {budget}
Travel Interests: {', '.join(interests)}

IMPORTANT:
- Generate itinerary for EXACTLY {days} days.
- Create separate detailed section for each day from Day 1 to Day {days}.
- Do NOT skip any day.
- Do NOT stop early.
- Make each day unique.
- Adjust activities based on budget.
- Focus strongly on selected interests.
- Use proper markdown formatting.

Format:

## {destination} {days} Days & {nights} Nights Itinerary

Write a short introduction paragraph.

Then generate:

**Day 1:**
**Morning:** ...
**Afternoon:** ...
**Evening:** ...

Continue this format until:

**Day {days}:**
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        return response.text

    except Exception:
        # Fallback dynamic version
        fallback = f"""
## {destination} {days} Days & {nights} Nights Itinerary

This personalized itinerary focuses on {', '.join(interests)} experiences under a {budget} budget.
"""

        for i in range(1, days + 1):
            fallback += f"""

**Day {i}:**
**Morning:** Explore main attractions.
**Afternoon:** Enjoy local experiences.
**Evening:** Relax and explore markets.
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
