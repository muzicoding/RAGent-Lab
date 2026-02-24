from langchain_ollama import OllamaEmbeddings

# 不传model，默认用的是text-embeddings-v1
model = OllamaEmbeddings(model="qwen3-embedding:4b",
                         base_url="http://10.190.15.2:11434")

# embed_query, embed_document
print(model.embed_query("我喜欢你"))
print(model.embed_documents(["我喜欢你", "我稀饭你", "晚上吃啥"]))
