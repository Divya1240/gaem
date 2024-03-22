import streamlit as st

# Set a funky background
st.markdown(
    """
    <style>
    body {
        background-image: url("https://i.pinimg.com/originals/15/96/3f/15963fe748b9eb99b7b5e9e8aa4252ac.gif");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("Patient Registration App")

# Sidebar for patient information
with st.sidebar:
    st.header("Enter Patient Information")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=150, step=1)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    address = st.text_area("Address")
    phone = st.text_input("Phone Number")

# Display patient information
st.write("## Patient Information")
st.write(f"**Name:** {name}")
st.write(f"**Age:** {age}")
st.write(f"**Gender:** {gender}")
st.write(f"**Address:** {address}")
st.write(f"**Phone Number:** {phone}")

# Button to submit
if st.button("Submit"):
    st.success("Patient information submitted successfully!")
