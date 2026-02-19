from dashscope import api_key
from openai import OpenAI
# 1. 获取Client对象
client = OpenAI(
    # base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
    base_url="http://10.190.15.2:11434/v1",
    api_key=""
)

# 2. 调用模型
response = client.chat.completions.create(
    model="qwen3:8b",
    messages=[
        {"role": "system", "content": "你是一个Python编程专家，并且不说废话简单回答"},
        {"role": "assistant", "content": "好的，我是编程专家，并且话不多，你要问什么？"},
        {"role": "user", "content": "输出1-10的数字，使用python代码"}
    ]
)

# 3. 处理结果
print(response.choices[0].message.content)