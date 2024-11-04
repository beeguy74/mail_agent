from dotenv import load_dotenv
from sys import argv
from pathlib import Path
from langchain_google_community import GmailToolkit
from langgraph.prebuilt import create_react_agent
import os
from langchain_openai import ChatOpenAI


load_dotenv()

# it uses openrouter api key but it should be named openau_api_key
llm = ChatOpenAI(model="openai/gpt-4o-mini-2024-07-18", temperature=0.6, openai_api_key=os.environ["OPENAI_API_KEY"], openai_api_base="https://openrouter.ai/api/v1")

toolkit = GmailToolkit()
tools = toolkit.get_tools()
agent_executor = create_react_agent(llm, tools)

if __name__ == '__main__':

    while True:
        question = input("\033[92mPosez votre question ou tapez 'q' pour quitter: \033[0m")
        if question == 'q':
            break
        events = agent_executor.stream(
            {"messages": [("user", question)]},
            stream_mode="values",
        )
        for event in events:
            event["messages"][-1].pretty_print()