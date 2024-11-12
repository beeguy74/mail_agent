import gradio as gr
from test import agent_executor
import re
import json

def chat_with_agent(question):
    events = agent_executor.stream(
        {"messages": [("user", question)]},
        stream_mode="values",
    )
    responses = []
    for event in events:
        content = event["messages"][-1].content
        # Parse JSON content and format it for better readability
        try:
            json_content = json.loads(content)
            formatted_content = json.dumps(json_content, indent=4)
        except json.JSONDecodeError:
            formatted_content = content
        responses.append(formatted_content)
    return "\n".join(responses)

iface = gr.Interface(
    fn=chat_with_agent,
    inputs="text",
    outputs="text",
    title="Chat with Agent",
    description="Ask questions to the agent and get responses."
)

if __name__ == "__main__":
    iface.launch()
