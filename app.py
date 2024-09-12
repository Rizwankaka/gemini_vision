from dotenv import load_dotenv
load_dotenv() # load environmnet variables from .env file 

# importing the packages 
import streamlit as st 
import os 
import google.generativeai as genai 
from PIL import Image

# configure API key for Google Generative AI 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# loading gemini model and get responses 
model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input, image):
    if input!='':
        # Generate response with both text and image
        response= model.generate_content([input, image])
    else:
        # Generate response with image input only 
        response = model.generate_content(image)

    return response.text

# initialize streamlit app 
st.set_page_config(page_title='Vision AI App', page_icon='🤖')

st.header('Gemini Vision Application')
input= st.text_input("Input Prompt", key = 'input')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "gif"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

# Submit button to get response 
submit = st.button("Tell me about the image")

# if submit button is clicked 
if submit:
    response = get_gemini_response(input, image)
    st.subheader('The Response is')
    st.write(response)