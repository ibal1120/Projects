import streamlit as st

# Function to compute day of week using Zeller’s Congruence
def get_day_of_week(year, month, day):
    original_year = year
    if month == 1:
        month = 13
        year -= 1
    elif month == 2:
        month = 14
        year -= 1

    j = year // 100
    k = year % 100

    H = (day + (26 * (month + 1) // 10) + k + (k // 4) + (j // 4) + (5 * j)) % 7
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[H]

# Streamlit UI
st.title("📅 Day of the Week Finder")

year = st.number_input("Enter the year:", min_value=1, value=2024)
month = st.number_input("Enter the month (1-12):", min_value=1, max_value=12, value=6)
day = st.number_input("Enter the day of the month (1-31):", min_value=1, max_value=31, value=24)

if st.button("Find Day"):
    try:
        weekday = get_day_of_week(year, month, day)
        st.success(f"The day for {year}-{month:02}-{day:02} is: **{weekday}**")
    except Exception as e:
        st.error(f"An error occurred: {e}")
