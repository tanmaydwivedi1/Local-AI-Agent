from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


model = ChatOllama(model="llama3.2")

template = """You are an expert in answering questions about the Pizza restaurent.

Here are some reviews: {reviews}

Here is the question to answer: {question}"""

prompt = ChatPromptTemplate(template)
chain = prompt | model

result = chain.invoke({"reviews": [], "question": "What is the best pizza in town?"})
print(result)