import ollama


def ask_llama(prompt: str) -> str:
    response = ollama.generate(
        model="llama3.2",
        prompt=prompt
    )
    return response["response"]
