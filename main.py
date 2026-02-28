from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from vector import retriver

model = ChatOllama(model="llama3.2")

template = """You are an expert in answering questions about the Pizza restaurent.

Here are some reviews: {reviews}

Here is the question to answer: {question}"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    print("\n\n-------------------------------------------------------------")
    question = input("Enter your question or (q) to quit:")

    print("\n\n")
    if question.lower() == "q":
        break
    reviews = retriver.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)