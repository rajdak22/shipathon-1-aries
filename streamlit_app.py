# shipathon-1-aries
# Streamlit code for project 4, ARIES SHIPATHON
import streamlit as st
import pandas as pd

# Set the page configuration
st.set_page_config(
    page_title="Event Suggestor",
    page_icon="📅",
    layout="centered",
)

# Heading
st.title("Welcome to Event Suggestor 📅")

# Instruction for selecting interests
st.write("### Instruction:")
st.markdown("1. Select the options which interest you.")

# Placeholder for dynamically generated buttons (Step 3 is intentionally left for later implementation)

# Instruction for selecting free time slots
st.write("### Instruction:")
st.markdown("2. Below are hour-wise slots from **9:00 to 22:00**. Select the time slots during which you are free:")

# Initialize session state for storing free time selections
if "free_time" not in st.session_state:
    st.session_state.free_time = []

# Hour-wise slots from 9:00 to 22:00
time_slots = [f"{hour}:00" for hour in range(9, 23)]

# Display buttons for each time slot
st.write("### Select your free time slots:")

for slot in time_slots:
    if st.button(slot):
        # Append the selected slot to the free_time list if not already selected
        if slot not in st.session_state.free_time:
            st.session_state.free_time.append(slot)

# Display the selected free time slots
st.write("### Your Selected Free Time Slots:")
st.write(st.session_state.free_time)
