from dotenv import load_dotenv
from langchain_google_community import GmailToolkit
from langgraph.prebuilt import create_react_agent
import os
from langchain_openai import ChatOpenAI

# Correct the environment variable name
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="openai/gpt-4o-mini-2024-07-18", temperature=0.6, openai_api_key=openai_key, openai_api_base="https://openrouter.ai/api/v1")


toolkit = GmailToolkit()
tools = toolkit.get_tools()
agent_executor = create_react_agent(llm, tools)

if __name__ == '__main__':
    # Import the Gradio interface
    from interface import iface
    iface.launch()