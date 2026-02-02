"""
    MAC中配置OPENAI的APIKEY环境变量方法：
    1. 从服务商获取APIKEY，这里采用的是阿里云百炼平台（https://bailian.console.aliyun.com/）
    2. 在终端（Terminal）中输入`open .zshrc`，进入编辑环境变量名
        `export OPENAI_API_KEY="sk-71ec2ae3*********ea1b525809"`
        `export DASHSCOPE_API_KEY="sk-71ec2ae3*********ea1b525809"`
    3. 保存并重启PyCharm
"""

import os
from openai import OpenAI

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    # api_key="sk-71ec2ae3*********ea1b525809", # 配置完环境变量后就不用明文写在这了
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",

    # Ollama本地url
    # base_url="http://localhost:11434/v1"
)

completion = client.chat.completions.create(
    model="qwen3-max",
    # model="qwen3:8b", # 本地8b模型
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你是谁？"},
    ],
    stream=True
)
for chunk in completion:
    print(chunk.choices[0].delta.content, end="", flush=True)