import re
import os
import dotenv
from llm_client import OpenAICompatibleClient
import skill
import tools

dotenv.load_dotenv()

# --- 1. 配置LLM客户端 ---
# 请根据您使用的服务，配置对应的凭证和地址
API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
MODEL_ID = "qwen3-max"
TAVILY_API_URL = os.getenv("TAVILY_API_URL")

llm = OpenAICompatibleClient(
    model=MODEL_ID,
    api_key=API_KEY,
    base_url=BASE_URL
)

# --- 2. 初始化 ---
user_prompt = "你好，请帮我查询一下今天北京的天气，然后根据天气推荐一个合适的旅游景点。"
prompt_history = [f"用户请求：{user_prompt}"]

print(f"用户输入: {user_prompt}\n" + "="*40)

# --- 3. 执行主循环 ---
for i in range(10): # 设置最大循环次数
    print(f"--- 循环 {i+1} ---\n")

    # 3.1 构建prompt
    full_prompt = "\n".join(prompt_history)

    # 3.2 调用llm进行思考
    llm_output = llm.generate(full_prompt, system_prompt=skill.AGENT_SYSTEM_PROMPT)
    # 模型可能会输出多余的Thought-Action，需要截断
    match = re.search(r'(Thought:.*?Action:.*?)(?=\n\s*(?:Thought:|Action:|Observation:)|\Z)', llm_output, re.DOTALL)
    if match:
        truncate = match.group(1).strip()
        if truncate != llm_output.strip():
            llm_output = truncate
            print("已截断多余的 Thought-Action 对")
        print(f"模型输出:\n{llm_output}\n")
        prompt_history.append(llm_output)

    # 3.3. 解析并执行行动
    action_match = re.search(r"Action: (.*)", llm_output, re.DOTALL)
    if not action_match:
        observation = "错误: 未能解析到 Action 字段。请确保你的回复严格遵循 'Thought: ... Action: ...' 的格式。"
        observation_str = f"Observation: {observation}"
        print(f"{observation_str}\n" + "=" * 40)
        prompt_history.append(observation_str)
        continue
    action_str = action_match.group(1).strip()

    if action_str.startswith("Finish"):
        final_answer = re.match(r"Finish\[(.*)\]", action_str).group(1)
        print(f"任务完成，最终答案: {final_answer}")
        break

    tool_name = re.search(r"(\w+)\(", action_str).group(1)
    args_str = re.search(r"\((.*)\)", action_str).group(1)
    kwargs = dict(re.findall(r'(\w+)="([^"]*)"', args_str))

    if tool_name in tools.available_tools:
        observation = tools.available_tools[tool_name](**kwargs)
    else:
        observation = f"错误:未定义的工具 '{tool_name}'"

    # 3.4. 记录观察结果
    observation_str = f"Observation: {observation}"
    print(f"{observation_str}\n" + "=" * 40)
    prompt_history.append(observation_str)





