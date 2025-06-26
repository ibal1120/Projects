import streamlit as st

st.set_page_config(page_title="CSN Tuition & Number App", page_icon="📘", layout="centered")

# Custom CSN-inspired styling
csn_blue = "#003865"
csn_gold = "#FFC72C"
st.markdown(f"""
    <style>
        body {{
            background-color: #f7f9fc;
        }}
        .main {{
            color: {csn_blue};
        }}
        .stButton>button {{
            background-color: {csn_blue};
            color: white;
            border-radius: 8px;
            padding: 8px 16px;
        }}
        .stButton>button:hover {{
            background-color: {csn_gold};
            color: black;
        }}
        .css-1v3fvcr p {{
            color: {csn_blue};
        }}
    </style>
""", unsafe_allow_html=True)

st.title("CSN Tuition & Number Analyzer")
st.subheader("| Powered by Streamlit |")

# Menu
menu = st.sidebar.selectbox("Choose an Option", ["Tuition Calculator", "Number Statistics", "Exit"])

if menu == "Tuition Calculator":
    st.header("Tuition Calculator")

    tuition = st.number_input("How much is your college tuition?", min_value=1)
    tuition_increase = st.number_input("What is the percent increase every year?", min_value=1)
    time_line = st.number_input("How many years are you going to college?", min_value=1)

    if st.button("Calculate Tuition"):
        st.write("### Yearly Tuition Projection")
        st.write(f"1: ${tuition:,.2f}")
        current = tuition
        for year in range(2, time_line + 1):
            current += current * (tuition_increase / 100)
            st.write(f"{year}: ${current:,.2f}")

elif menu == "Number Statistics":
    st.header("Number Statistics")
    st.write("Enter numbers one at a time. Use **-99** to stop and see your results.")

    numbers = []
    num = st.number_input("Enter an integer", step=1)

    if "numbers" not in st.session_state:
        st.session_state.numbers = []

    if st.button("Add Number"):
        if num != -99:
            st.session_state.numbers.append(num)
        else:
            numbers = st.session_state.numbers

    if st.button("Show Results") and st.session_state.numbers:
        numbers = st.session_state.numbers
        odd = [n for n in numbers if n % 2 != 0]
        even = [n for n in numbers if n % 2 == 0]

        st.write("### Statistics")
        st.write(f"Sum of odd numbers: {sum(odd):.2f}")
        st.write(f"Sum of even numbers: {sum(even):.2f}")
        st.write(f"Average of odd numbers: {sum(odd)/len(odd):.2f}" if odd else "Average of odd numbers: N/A")
        st.write(f"Average of even numbers: {sum(even)/len(even):.2f}" if even else "Average of even numbers: N/A")
        st.write(f"Average of all numbers: {sum(numbers)/len(numbers):.2f}")
        st.write(f"Lowest number: {min(numbers):.2f}")
        st.write(f"Highest number: {max(numbers):.2f}")
        st.session_state.numbers = []

elif menu == "Exit":
    st.warning("App exited. Refresh the page to restart.")