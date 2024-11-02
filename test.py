from dotenv import load_dotenv
from sys import argv
from pathlib import Path
from modules.init import init_models
from llama_index.core import Settings
from llama_index.core.llms import ChatMessage
from langchain_google_community import GmailToolkit

toolkit = GmailToolkit()


if __name__ == '__main__':
    load_dotenv()
    

    llm = init_models("cohere/command-r")
    Settings.llm=llm
    Settings.chunk_size=2048

    while True:
        question = input("\033[92mPosez votre question par rapport au code du travail ou tapez 'q' pour quitter: \033[0m")
        if question == 'q':
            break
        # on cherche la reponse dans le code du travail
        message = ChatMessage(role="user", content=question)
        resp = llm.chat([message])
        print(resp)