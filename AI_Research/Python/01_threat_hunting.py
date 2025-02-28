from langchain_openai import OpenAI
from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from langchain.agents import Tool
from langchain.agents import initialize_agent
from langchain_core.tools import tool

load_dotenv()

client = OpenAI(api_key=os.getenv('API-KEY'))

@tool
def trigger_alert(to_email: str, subject: str, body: str):
    """
    Function used to raise alerts when something suspicious happened
    """
    from_email = "agent@saas.com"
    password = os.getenv('EMAIL_PASS') 

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.saas.com', 587)  
        server.starttls()  
        server.login(from_email, password)          
        
        server.send_message(msg)
        print("Email sent successfully!")
        
    except Exception as e:
        print(f"Failed to send email: {e}")
        
    finally:
        server.quit()  

def read_logs(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
        return file_contents
        
def main():
    
    log_content = read_logs("saas.log")

    tools = [  
    Tool(
        name="trigger_alert",
        func=trigger_alert,
        description="Function used to raise alerts when something suspicious happened")
    ]

    agent = initialize_agent(tools, client, agent="zero-shot-react-description", verbose=True, return_intermediate_steps=True)
    agent(f""" Read the content of this log file: ${log_content}, 
          and find any threats or indication of compromise. 
          If you find anything, call the trigger_alert function, 
          and send an email to admin at saas.com, with a reasonable subject and body.
                """)
    
if __name__ == "__main__":
    main()