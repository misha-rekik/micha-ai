from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate


template = (
        "Write a concise and ordered events within the  summary '{book_title}' in precise and short bullet points, "
        "Each bulletpoint should mention:\n"
        "- The key scenes and their components\n"
        "- The placement and interaction of characters within these scenes\n"
        "- The lighting and atmosphere of the scenes\n"
        "- How the setting looks and the general mood it conveys\n\n"
    )

PROMPT = PromptTemplate(template=template, input_variables=["book_title"])

EXAMPLE_PROMPT = PromptTemplate(
    template=template,
    input_variables=["book_title"],
)