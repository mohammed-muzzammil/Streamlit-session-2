import streamlit as st
import pandas as pd


# Title
st.title("Hello World")

# Text input
name = st.text_input("Enter your name", "Type here")
if name:
    st.write("Hello, ", name)

# Number input
age = st.number_input("Enter your age", min_value=0, max_value=100)
if age:
    st.write("You are ", age, " years old")

# Selectbox
occupation = st.selectbox("what is your occupation", ["None", "Student", "Teacher", "Doctor"])
if occupation == "None":
    occupation = st.text_input("Enter your occupation", "Type here")

# Multi-Selectbox
occupations = st.multiselect("what are your occupations", ["None", "Student", "Teacher", "Doctor"])
if occupations:
    st.write("You are a ", occupations)

# Checkbox
ocu = st.checkbox("Are you a student?")
st.write(ocu)
if ocu:
    st.write("You are a student")

# Radio
ocu = st.radio("What is your occupation", ["None", "Student", "Teacher", "Doctor"])
if ocu == "None":
    ocu = st.text_input("Enter your occupation")

# Slider
age = st.slider("How old are you?", min_value=0, max_value=1000)


# Button
button = st.button("Click me")
if button:
    st.write("You clicked the button")

# Date input
date = st.date_input("When is your birthday?")
if date:
    st.write("Your birthday is ", date)

# File Upload
file = st.file_uploader("Upload your file", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.write(df)

if file:
    st.download_button(
         label="Download data as CSV",
         data=file,
         file_name='large_df.csv',
         mime='text/csv',
     )

# Format for the data
st.markdown('Streamlit is **_really_ cool**.')
