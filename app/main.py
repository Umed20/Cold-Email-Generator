import streamlit as st 
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_website_text

def create_streamlit_app(llm, portfolio, clean_website_text):
    st.title("Cold Email Generator")
    url_input = st.text_input("Enter a Job URL")
    name_input = st.text_input("Enter your name")
    your_summary = st.text_input("Write your profile summary in 2 to 3 lines")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_website_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('Skills',[])
                links = portfolio.query_links(skills)
                email = llm.write_email(job,links,name_input,your_summary)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator")
    create_streamlit_app(chain,portfolio,clean_website_text)








