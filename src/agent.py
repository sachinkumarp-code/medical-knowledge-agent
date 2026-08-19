import os
import pandas as pd
import sqlite3
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import Chroma
from langgraph.prebuilt import create_react_agent


load_dotenv()

llm = ChatGroq(model="qwen/qwen3.6-27b")
embedding_model = HuggingFaceBgeEmbeddings(model_name = "all-MiniLM-L6-v2")
db = Chroma(persist_directory="data/chroma_db", embedding_function=embedding_model)

@tool
def search_medical_guidelines(query):
    """Searches clinical guidelines to answer medical questions"""
    result = db.similarity_search(query, k=1)
    return result[0].page_content

@tool
def query_patient_database(query):
    """Queries the hospital's SQLite database to answer questions about patient records.
    The database contains a single table named 'patients'.
    The exact column names are: patient_id, age, gender, cholesterol_level, and Diagnosis.
    Always use these exact column names when writing your SQL query."""
    conn = sqlite3.connect('data/patient_db.db')
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df.to_string()

tools = [search_medical_guidelines, query_patient_database]
agent = create_react_agent(llm, tools)

if __name__ == "__main__":

    print("\n🤖 Medical AI Agent Online! (Type 'quit' to exit)")
    print("-" * 50)

    while True:
        user_question = input("\nDoctor: ")

        if user_question.lower() in ['quit', 'exit']:
            print("Shutting down...")
            break

        response = agent.invoke({"messages": [("user", user_question)]})
        print(f"\nAgent: {response['messages'][-1].content}")
