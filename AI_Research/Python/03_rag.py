from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import openai
from langchain_core.tools import tool
from pydantic import BaseModel
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from langchain.agents import initialize_agent
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

client = OpenAI(api_key=os.getenv('API-KEY'))

class Incident(BaseModel):
    summary: str
    priority: str
    severity: str
    
    
def rag():
    loader = WebBaseLoader("https://cloud.google.com/docs/security/incident-response")
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    all_splits = text_splitter.split_documents(data)

    local_embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = Chroma.from_documents(documents=all_splits, embedding=local_embeddings)
    question = "What would be the priority and the severity of this incident: 2023-02-20 14:30:00,172 INFO [com.example.auth] - UNAUTHORIZED Authentication attempt from 192.168.1.100 for user 'admin' with admin privileges with password 'P@ssw0rd' was successful. Session ID: 1234567890."

    docs = vectorstore.similarity_search(question)
    len(docs)
    model = ChatOllama(model="llama3.1:8b",)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    
    RAG_TEMPLATE = """
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.


Answer the following question:

    {question}"""

    rag_prompt = ChatPromptTemplate.from_template(RAG_TEMPLATE)

    chain = (
        RunnablePassthrough.assign(context=lambda input: format_docs(input["context"]))
        | rag_prompt
        | model
        | StrOutputParser()
    )

    docs = vectorstore.similarity_search(question)

    print(chain.invoke({"context": docs, "question": question}))

def analyze_incident(incident):

    prompt = f"""
        You need to create an incident based on the following logs or security events: ${incident} 
    """
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": prompt},
    ],
    tools=[
        openai.pydantic_function_tool(Incident),
    ]
    )
        
    return response.choices[0].message.tool_calls[0].function.arguments


@tool
def send_email(subject: str, to_email: str, body: str):
    """
    Function used to send emails to an address with a subject and a body.
    """
    from_email = "Bob@organization.com"
    password = os.getenv('EMAIL_PASS') 

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.organization.com', 587)  
        server.starttls()  
        server.login(from_email, password)          
        
        server.send_message(msg)
        print("Email sent successfully!")
        
    except Exception as e:
        print(f"Failed to send email: {e}")
        
    finally:
        server.quit() 
        
def main():
    response = analyze_incident("2023-02-20 14:30:00,172 INFO [com.example.auth] - Authentication attempt from 192.168.1.100 for user 'admin' with password 'P@ssw0rd' succeeded. Session ID: 1234567890")
    json_object = json.loads(response)
    print(json_object)
    rag()
    

if __name__ == "__main__":
    main()