import streamlit as st
import requests

# Title
st.title("Image Colorizer")

# File uploader to upload black and white image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

# Text input
text = st.text_input("Enter a text...")

if st.button("Text to image"):
    r = requests.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': text,
        },
        headers={'api-key': '6d0a5321-5e74-4a0a-80e1-fc6a530846f5'}
    )
    print(r.json())
    st.write(r.json()['output_url'])

