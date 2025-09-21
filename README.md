# Recepie-Generator

Recepie-Generator is a Python application that generates **at least 3 recipes** based on the ingredients you have on hand.  
It also recommends additional ingredients to make the recipes more delicious.

## Tech Stack
- Python
- LangChain 
- Gemini 2.5 Flash API  
- Streamlit
- Streamlit Lottie (for animations)
## Preview Online
https://recepie-generator-2412.streamlit.app/

## Preview Locally

### Prerequisites
Make sure to have VsCode and python installed
- [VS Code](https://code.visualstudio.com/)  
- [Python](https://www.python.org/downloads/)
### Steps
Then open a folder in VsCode where you want to preview, and run these commands in terminal.
- git clone https://github.com/UzzmaShahid/Recepie-Generator.git
- cd Recepie-Generator
- pip install -r requirements.txt
- (Note: This project requires a Gemini API key to generate recipes.
  Create a file named .env in the project root and add your key like this: GEMINI_API_KEY=your_api_key_here
)
- streamlit run main.py
  
- <img width="873" height="639" alt="image" src="https://github.com/user-attachments/assets/59f6e850-9d9d-41f7-8746-5229d9cda91b" />


