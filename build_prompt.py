def build_prompt(question, chunks):
    context = "\n\n".join(chunks)
    return f""" Only by using the context given , answer the employee's question with no more than 3 lines. If you are unsure convey the same
    context:
    {context}
    question:
    {question}"""
    
    
if __name__ == "__main__":
    chunks = [
        "To reset your password, go to Account Settings.",
        "Refunds are processed within 5-7 business days.",
    ]
    print(build_prompt("How do I reset my password?", chunks))    