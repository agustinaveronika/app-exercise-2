import streamlit as st
import requests

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
        "https://70d9-103-82-14-56.ngrok-free.app/zodiac",
        
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
