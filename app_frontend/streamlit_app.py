import streamlit as st
import requests
import os
from dotenv import load_dotenv

if os.path.isfile('.env'):
    load_dotenv()

API_FLASK_CONVERT = "https://0636-2404-8000-1001-a561-2c59-4abe-4947-4816.ngrok-free.app/zodiac" if os.getenv("API_FLASK_CONVERT") is None else os.getenv("API_FLASK_CONVERT")
st.title("Zodiac Finder:stars:")

name = st.text_input("What is your name?")

# List of month
month_names = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

# To select months
month = st.selectbox("Select your birth month", month_names)

# To select days
day = st.selectbox("Select your birth date", range(1, 32))

# Display zodiac result
if st.button("Check your zodiac"):
    response = requests.post(
        # "https://70d9-103-82-14-56.ngrok-free.app/zodiac",
        API_FLASK_CONVERT,
        json={"name": name, "month": month, "day": day}
    )
    if name.strip():  # Check if name is not empty 
        if response.status_code == 200:
            result = response.json().get("zodiac")
            st.write(f"Hello {name}:wave:")
            st.write(f"Your Zodiac is {result}:star2:")
        else:
            st.error("Error to check your Zodiac")
    else:
        st.warning("Please enter your name :pensive:")
