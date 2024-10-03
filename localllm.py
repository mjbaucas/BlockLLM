import sys
import time
from langchain_community.llms import Ollama

llm = Ollama(
    model=sys.argv[1],
)

while True:
    question = input("Ask me a question: ")
    if question == "stop":
        sys.exit(1)
        
    start = time.time()
    for chunk in llm.stream(question):
        print(chunk, end="", flush=True) 
    end = time.time()
    print("\n")
    print(end-start)

    
# tinyllama - 637 MB - 49.64 - 42.46 - 42.63 - 34.76 - 37.60 - 37.97 - 43.41 - 31.95 - 40.18 - 49.15
# phi3:mini - 2.2 GB - 179.41 - 297.77 - 288.57 - 300.58 - 241.41 - 388.46 - 243.12 - 565.05 - 369.82 - 306.70
# phi       - 1.6 GB - 100.20 - 96.18 - 302.06 -  # Sometimes gives the wrong answer or rambles on too much
# gemma:2b  - 1.7 GB - 105.54 - 97.27 - 80.59 - 75.79 - 77.73 - 88.19 - 69.38 - 80.22 - 77.63 - 87.85
# qwen      - 2.3 GB - 101.48 - 113.71 - 98.11 - 75.44 - 71.44 - 70.54 - 90.70 - 75.04 - 86.16 - 78.62
