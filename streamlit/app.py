import streamlit as st
from langchain.llms import OpenAI


openai_api_key = st.sidebar.text_input('OpenAI API Key')


with st.form('form'):
  text = st.text_area('Enter text:', '')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(text))