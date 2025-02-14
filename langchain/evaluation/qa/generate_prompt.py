# flake8: noqa
from langchain.prompts import PromptTemplate
from langchain.prompts.base import RegexParser

template = """You are a teacher coming up with questions to ask on a quiz. 
Given the following document, please generate a question and answer based on that document.

Example Format:
<Begin Document>
...
<End Document>
QUESTION: question here
ANSWER: answer here

These questions should be detailed and be based explicitly on information in the document. Begin!

<Begin Document>
{doc}
<End Document>"""
output_parser = RegexParser(
    regex=r"QUESTION: (.*?)\nANSWER: (.*)", output_keys=["question", "answer"]
)
PROMPT = PromptTemplate(
    input_variables=["doc"], template=template, output_parser=output_parser
)
