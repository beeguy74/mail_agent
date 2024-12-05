from dotenv import load_dotenv
from sys import argv
from pathlib import Path
from langchain_google_community import GmailToolkit
from langgraph.prebuilt import create_react_agent
import os
from langchain_openai import ChatOpenAI
import base64
from modules.pdf_to_image import pdf_page_to_base64
from modules.server import app
from IPython.display import Image as IPImage
from langchain_core.messages import HumanMessage


load_dotenv()

# it uses openrouter api key but it should be named openau_api_key
llm = ChatOpenAI(model="openai/gpt-4o-mini", temperature=0.6, openai_api_key=os.environ["OPENAI_API_KEY"], openai_api_base="https://openrouter.ai/api/v1")

from IPython.display import display

file_path = Path("./NeverovCV.pdf")

base64_image = pdf_page_to_base64(file_path, 0)
display(IPImage(data=base64.b64decode(base64_image)))


query = "What is the name of the person in CV?"

def message_with_image(query):
    message = HumanMessage(
        content=[
            {"type": "text", "text": query},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
            },
        ],
    )
    return message

toolkit = GmailToolkit()
tools = toolkit.get_tools()
llm.invoke
# agent executor gives more comprehensive output
# agent_executor = create_react_agent(llm, tools)
llm_with_tools = llm.bind_tools(tools)

if __name__ == '__main__':
    app.run(debug=True)

    while True:
        question = input("\033[92mPosez votre question ou tapez 'q' pour quitter: \033[0m")
        if question == 'q':
            break
        response = llm_with_tools.invoke([message_with_image(question)])
        response.pretty_print()
        # events = agent_executor.stream(
        #     {"messages": [message_with_image(question)]},
        #     stream_mode="values",
        # )
        # for event in events:
        #     event["messages"][-1].pretty_print()