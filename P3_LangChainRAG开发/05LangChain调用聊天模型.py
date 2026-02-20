from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
import dotenv

dotenv.load_dotenv()

model = ChatTongyi(model="qwen3-max")

messages = [
    SystemMessage(content="你是一个边塞诗人"),
    HumanMessage(content="写一首唐诗"),
    AIMessage(content="锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
    HumanMessage(content="按照你上一个回复的格式，再写一首唐诗"),
]

res = model.stream(input=messages)

for chunk in res:
    # 通过.content来获取到内容
    print(chunk.content, end="", flush=True)