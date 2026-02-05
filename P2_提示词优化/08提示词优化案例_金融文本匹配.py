import os
import dotenv
from openai import OpenAI

dotenv.load_dotenv()
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

examples_data = {
    "是": [
        ("公司ABC发布了季度财报,显示盘利增长。", "财报披露,公司ABC利润上升。"),
        ("公司ITCAST发布了年度财报,显示蛋利大幅度增长。", "财报按露,公司ITCAST更赚钱了。")
    ],
    "不是": [
        ("黄金价格下践,投资者抛售。", "外汇市场文易额创下新高。"),
        ("央行降息,制激经济增长。", "新能源技术的创新。")
    ]
}

questions = [
    ("利率上升,影响房地产市场。","高利率对房地产有一定的冲击。"),
    ("油价大幅度下跌,能源公司面临挑战。","未来智能城市的建设趋势越加明显。"),
    ("股票市场今日大涨,投资者乐观。","持续上涨的市场让投资者感到满意。")
]

messages = [
    {"role": "system", "content": "判断2个句子语义是否相似，相似句子返回是，不相似句子返回不是，不要其他回答"}
]


for key, value in examples_data.items():
    for t in value:
        messages.append({"role": "user", "content": f"句子1：{t[0]}, 句子2：{t[1]}"})
        messages.append({"role": "assistant", "content": key})

# for message in messages:
#     print(message)

for question in questions:
    response = client.chat.completions.create(
        model="qwen3-max",
        messages=messages + [{"role": "user", "content": f"句子1：{question[0]}, 句子2：{question[1]}"}]
    )
    print(response.choices[0].message.content)