from langchain_community.llms import Ollama

SYSTEM_PROMPT = """
You are a helpful, respectful, and honest AI assistant. Always strive to provide useful and accurate responses.
If you do not know the answer to a question, do not share incorrect information.
"""

def firePrompt(prompt: str, temp=0.4) -> str:
    llm = Ollama(model="llama3.2",
             system=SYSTEM_PROMPT,
             temperature=temp
             )
    res = llm.invoke(prompt)
    return res