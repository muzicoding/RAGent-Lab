from langchain_ollama import OllamaLLM
from openai import base_url

model = OllamaLLM(model="qwen3:8b",
                  base_url="http://10.190.15.2:11434")

res = model.invoke(input="你是谁呀能做什么？")

print(res)