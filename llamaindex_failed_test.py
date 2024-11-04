from dotenv import load_dotenv
from sys import argv
from pathlib import Path
from modules.init import init_models
from llama_index.core import Settings
from llama_index.core.llms import ChatMessage
from llama_index.tools.google import GmailToolSpec
from llama_index.tools.google import GoogleCalendarToolSpec
from llama_index.tools.google import GoogleSearchToolSpec
from llama_index.core.agent import ReActAgent

# from langchain_google_community import GmailToolkit

# toolkit = GmailToolkit()

tool_spec = GmailToolSpec()

# i think that googletoolSpec is outdated in llamaindex hub
if __name__ == '__main__':
    load_dotenv()
    

    llm = init_models("openai/gpt-4o-mini-2024-07-18")
    Settings.llm=llm
    Settings.chunk_size=2048
    agent = ReActAgent.from_tools(tool_spec.to_tool_list() , verbose=True)
    ## TypeError: GmailToolSpec.search_messages() missing 1 required positional argument: 'query'
    print(tool_spec.load_data())


    while True:
        question = input("\033[92mPosez votre question par rapport au code du travail ou tapez 'q' pour quitter: \033[0m")
        if question == 'q':
            break
        # on cherche la reponse dans le code du travail
        message = ChatMessage(role="user", content=question)
        resp = agent.chat([message])
        print(resp)