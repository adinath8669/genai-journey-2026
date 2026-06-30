import streamlit as st

st.title("Student Registration Form")

with st.form("student_form"):

    name = st.text_input("Enter your name")

    age = st.number_input(
        "Enter your age",
        min_value=1,
        max_value=100
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    course = st.selectbox(
        "Course",
        ["Python", "AI", "Machine Learning"]
    )

    address = st.text_area("Address")

    submit = st.form_submit_button("Submit")

if submit:
    st.success("Form Submitted Successfully!")

    st.write("### Student Details")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Gender:", gender)
    st.write("Course:", course)
    st.write("Address:", address)