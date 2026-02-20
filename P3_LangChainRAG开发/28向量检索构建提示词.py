'''
提示词 用户提问 + 向量库中检索到的参考资料
'''
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatTongyi(model="qwen3-max")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "以我提供的已知参考资料为主，简洁和专业地回答用户问题。参考资料：{context}。"),
        ("user", "用户提问：{input}")
    ]
)

vector_store = InMemoryVectorStore(
    embedding=DashScopeEmbeddings(model="text-embedding-v4")
)

# 准备一下资料（向量库数据）
# add_texts 传入一个list[str]
vector_store.add_texts(["减肥就是要少吃多练", "在减脂期间吃东西很重要，清淡少油控制卡路里摄入并运动起来", "跑步是很好的运动哦"])

input_text = "怎么减肥？"

# 检索向量库
result = vector_store.similarity_search(input_text, k=2)
refernce_text = "["
for doc in result:
    refernce_text += doc.page_content
refernce_text += "]"

def print_prompt(prompt):
    print(prompt.to_string())
    print("="*20)
    return prompt

# chain
chain = prompt | print_prompt | model | StrOutputParser()

res = chain.invoke(input={"input": input_text, "context": refernce_text})

print(res)
