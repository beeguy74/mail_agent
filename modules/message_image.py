
from IPython.display import display
from pathlib import Path
from modules.pdf_to_image import pdf_page_to_base64
from IPython.display import Image as IPImage
import base64
from langchain_core.messages import HumanMessage


display(IPImage(data=base64.b64decode(base64_image)))


query = "What is the name of the person in CV?"

def message_with_image(query, file_path):
    base64_image = pdf_page_to_base64(file_path, 0)
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