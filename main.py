from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st
import json
from streamlit_lottie import st_lottie

load_dotenv()
api_key =  os.getenv("GEMINI_API_KEY")  or st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash-lite")

# using animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
lottie_cooking = load_lottiefile("Cooking.json")

col1, col2, col3 = st.columns([1, 2, 1]) 
with col2:  
    st_lottie(
        lottie_cooking,
        speed=1,
        reverse=False,
        loop=True,
        height=200,
        width=200
    )
    
st.set_page_config(page_title="Recepie Generator", page_icon="✨")
st.title("Welcome to Recepie generator! ")
ingredients = st.text_input("Enter the ingredients")

prompt = f"""
You are a cook . You can recommend the recepies that can be made using the mentioned ingredients.
You must follow instructions carefully and stay within your expertise.
If the user input information is unclear or irrelavant, politely state the limitations instead of making up facts.
If the user input is irrelavant ,respond politely that Please mention the ingredients.
Also add some emojies for actively engaging with the user.


Based on user input of ingredients
ingredients = {ingredients}

Based on ingredients, provide :
1. 3 recepies that can be made with those ingredients.
2. Cooking time of each
3. Step by step instructions on how to make each recepie.
4. Recommend adding some other ingredient to make the recepie better.
"""

if st.button("Generate recepies"):
 with st.spinner("In progress ... "):
    result = model.generate_content(prompt)
    st.subheader("Full response")
    st.write(result.text)