import sys
import time
from langchain_community.llms import Ollama

#while True:
#    question = input("Ask me a question: ")
#    if question == "stop":
#        sys.exit(1)
 
models = [
    "granite3.2:2b",
    "llama3.2:1b",
    "gemma2:2b"    
]

questions = [
    "Define BMI and explain how it is calculated.",
    "Explain drip irrigation and why it is used in modern agriculture.",
    "What is cruise control, and how does it help during long trips?"
] 


for k in range(0, len(models)):
    llm = Ollama(
        model=models[k],
    )
    print(models[k])
    times_i = []
    for i in range(0, len(questions)):
        print(questions[i])
        times_j = []
        for j in range(0,10):
            start = time.time()
            output = llm.invoke(questions[i])
            end = time.time()
            elapsed = end-start
            times_j.append(elapsed)
            print(elapsed)
            print(output)
        
        sum_time_j = 0.0
        for time_j in times_j:
            sum_time_j+=time_j
        average_time_j = sum_time_j/len(times_j)
        print("Average Time: " + str(average_time_j))
        times_i.append(average_time_j)
        
    sum_time_i = 0.0
    for time_i in times_i:
        sum_time_i+=time_i
    average_time_i = sum_time_i/len(times_i)
    print("Overall average Time: " + str(average_time_i))

