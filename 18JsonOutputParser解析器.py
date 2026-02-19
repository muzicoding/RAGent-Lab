from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate

# 创建解析器
str_parser = StrOutputParser()
json_parser = JsonOutputParser()

# 模型创建
model = ChatTongyi(model="qwen3-max")

# 第一个提示词模板
first_tempalte = PromptTemplate.from_template(
    "我邻居姓:{lastname}，刚生了{gender}, 请起名，并封装为JSON格式返回给我，"
    "要求key是name，value是你起的名字，请严格遵守规则。"
)

# 第二个提示词模板
second_template = PromptTemplate.from_template(
    "姓名{name}, 请帮我解析含义。"
)

# 构建链
chain = first_tempalte | model | json_parser | second_template | model | str_parser

for chunk in chain.stream({"lastname": "张", "gender": "女儿"}):
    print(chunk, end="", flush=True)
