from urllib import response
import streamlit as st
from langchain_experimental.agents import create_csv_agent
from langchain_openai import OpenAI
from dotenv import load_dotenv


def main():
    
    load_dotenv()
    
    st.set_page_config(page_title="Ask you data📊")
    st.header("Ask your Data 📊")
    
    user_csv = st.file_uploader("Upload your CSV", type='csv')
    
    if user_csv is not None:
        user_question = st.text_input("Ask a question about your data...")
 
        llm = OpenAI(temperature=0)
        agent = create_csv_agent(llm, user_csv, verbose=True)
    
        if user_question is not None and user_question !="":
            response = agent.run(user_question)
            st.write(f"You asked: {user_question}")
            st.write(f"{response}")
 
 
 
if __name__ == "__main__":
    main()    