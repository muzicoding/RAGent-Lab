import json
import os

from openai import OpenAI
import dotenv

dotenv.load_dotenv()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

schema =  ['日期', '股票名称', '开盘价', '收盘价', '成交量']
# 示例数据
examples_data = [
    {
        "content": "2023-01-10,股市蓝落,殷票强大科技A股今日开盘价100人民币,一度飙升至105人民币,随后回落至98人民币,最终以102人民币收盘,成交量达到520000。",
        "answers": {
            "日期": "2023-01-10",
            "股票名称": "强大科技A股",
            "开盘价": "100人民币",
            "收盘价": "102人民币",
            "成交量": "520000"
        }
    },
    {
        "content": "2024-05-16,股市利好。殷票英伟达美股今日开盘价105美元,一度飙升至109美元,随后回落至100美元,最终以116美元收盘,成文量达到3560000。",
        "answers": {
            "日期": "2024-05-16",
            "股票名称": "英伟达美股",
            "开盘价": "105美元",
            "收盘价": "116美元",
            "成交量": "3560000"
        }
    }
]
# 问题
questions = [
    "2023-01-10,股市蓝落,股票强科A股今日开盘价100人民币,一度飙升至105人民币,随后回落至98人民币,最终以102人民币收盘,成交量达到520000。",
    "2024-05-16,股市利好。股票英伟达美股今日开盘价105美元,一度飙升至109美元,随后回落至100美元,最终以116美元收盘。",
]

messages = [
    {"role": "system", "content": "现在你需要帮助我完成信息抽取任务，当我给你一个句子时，你需要帮我抽取出句子中实体信息，并按照JSON的格式输出，上述句子中没有的信息用['原文中未提及']来表示，多个值之间用','分隔。"}
]

for example in examples_data:
    messages.append(
        {"role": "user", "content": example["content"]}
    )
    messages.append(
        {"role": "assistant", "content": json.dumps(example["answers"], ensure_ascii=False)})

# for message in messages:
#     print(message)

for question in questions:
    response = client.chat.completions.create(
        model="qwen3-max",
        messages=messages + [{"role": "user", "content": f"按照上面的示例，现在抽取这个句子的信息{question}"}]
    )
    print(response.choices[0].message.content)
