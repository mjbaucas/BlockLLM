import sys
from langchain_community.llms import Ollama

llm = Ollama(
    model="tinyllama",
)

while True:
    question = input("Ask me a question: ")
    if question == "stop":
        sys.exit(1)
    output = llm.invoke(
        question
    )
    print(f"\n{output}") 
