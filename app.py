# Importing the necessary modules from the Streamlit and LangChain packages
import streamlit as st
from langchain_community.llms import OpenAI

# Setting the title of the Streamlit application
st.title('Simple LLM-App 🤖')

# Creating a sidebar input widget for the OpenAI API key, input type is password for security
openai_api_key = st.sidebar.text_input('OpenAI API key', type='password')


# Defining a function to generate a response using the OpenAI language model
def generate_response(input_text):
  try:
    # Intitalizing the OpenAI language model with a specified temprature and API key
    llm = OpenAI(temperature = 0.7, openai_api_key = openai_api_key)
    # Displaying the generated response as an informational message in the Streamlit app
    respnse = llm.generate(prompt=input_text)
    return response
  except Exception as e:
    if 'rate_limit' in str(e).lower():
      return "Rate Limit exceeded. Please try again later."
    elif 'quota' in str(e).lower():
      return "Quata exceeded. Please check your OpenAI plan and billing details."
    else:
      return f"An error ocurred: {e}"


# Creating a form in the Streamlit app for user input
with st.form('my_form'):
  # Adding a text area for user input
  text = st.text_area('Enter text:','')
  # Adding a submit button for the form
  submitted = st.form_submit_button('Submit')
  # Displaying a warning if the entered API key does not start with 'sk-'
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  # If the form is submitted and the API key is valid, generate a response
  if submitted and openai_api_key.startswith('sk-'):
    response = generate_response(text)
    st.info(response)


