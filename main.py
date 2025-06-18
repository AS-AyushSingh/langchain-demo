#integrate our code OpenAi with the OpenAI API
import os
from constants import OPENAI_API_KEY
from langchain.llms import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

#streamlit framework
st.title("langchain demo with OpenAI")
input_text = st.text_input("Search the topic you want: ")

#OpenAI llms
llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.9)
if input_text:
    llm_response = llm(input_text)
    st.write(llm_response)
