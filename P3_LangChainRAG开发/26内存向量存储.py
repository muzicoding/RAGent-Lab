from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

vector_store = InMemoryVectorStore(
    embedding=DashScopeEmbeddings()
)

loader = CSVLoader(
    file_path="./data/info.csv",
    encoding="utf-8",
    source_column="source" # 指定本条数据的来源是哪里？
)

documents = loader.load()

# 向量存储的新增、删除、检索
vector_store.add_documents(
    documents=documents, # 被添加的文档，类型：list[Documents]
    ids=["id"+str(i) for i in range(1, len(documents)+1)] # 文档的id，类型：list[str]
)

# 删除
vector_store.delete(ids=["id1", "id2"])

# 检索
result = vector_store.similarity_search(
    query="Python是不是简单易学",
    k=3
)

print(result)
