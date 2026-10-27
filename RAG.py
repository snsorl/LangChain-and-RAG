documents = [
    "LangChain builds AI applications.",
    "LangGraph builds workflows with loops and multiple agents.",
    "RAG retrieves information before answering questions."
]

question = "What does LangGraph build?"

context = next(
    (doc for doc in documents if "LangGraph" in doc),
    "Information not found."
)

print("Question:", question)
print("Retrieved context and answer:", context)
