from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_chroma import Chroma

# Chroma 向量数据库（轻量级）
# 确保 langchain-chroma chromadb 这两个库安装了

vector_store = Chroma(
    collection_name="test",  # 当前向量存储起名，类似数据库的表名
    embedding_function=DashScopeEmbeddings(), # 嵌入模型
    persist_directory="./chroma_db" # 指定数据存放的文件夹
)

# loader = CSVLoader(
#     file_path="./data/info.csv",
#     encoding="utf-8",
#     source_column="source" # 指定本条数据的来源是哪里？
# )
#
# documents = loader.load()

# # 向量存储的新增、删除、检索
# vector_store.add_documents(
#     documents=documents, # 被添加的文档，类型：list[Documents]
#     ids=["id"+str(i) for i in range(1, len(documents)+1)] # 文档的id，类型：list[str]
# )
#
# # 删除
# vector_store.delete(ids=["id1", "id2"])

# 检索
result = vector_store.similarity_search(
    query="Python是不是简单易学",
    k=3,
    filter={"source": "黑马程序员"}
)

print(result)
