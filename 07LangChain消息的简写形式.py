from langchain_community.chat_models.tongyi import ChatTongyi
import dotenv

dotenv.load_dotenv()

model = ChatTongyi(model="qwen3-max")

# 动态，运行时langchain转换为Message类对象， 支持内部填充{变量}占位！！！！
messages = [
    # (角色，内容) 角色: system/human/ai
    ("system", "你是一个边塞诗人"),
    ("human", "写一首唐诗"),
    ("ai", "锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
    ("human", "按照你上一个回复的格式，再写一首唐诗")
]

res = model.stream(input=messages)

for chunk in res:
    # 通过.content来获取到内容
    print(chunk.content, end="", flush=True)