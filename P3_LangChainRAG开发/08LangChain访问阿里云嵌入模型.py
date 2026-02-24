from langchain_community.embeddings import DashScopeEmbeddings

import dotenv

dotenv.load_dotenv()

# 不传model，默认用的是text-embeddings-v1
model = DashScopeEmbeddings()

# embed_query, embed_document
print(model.embed_query("我喜欢你"))
print(model.embed_documents(["我喜欢你", "我稀饭你", "晚上吃啥"]))
