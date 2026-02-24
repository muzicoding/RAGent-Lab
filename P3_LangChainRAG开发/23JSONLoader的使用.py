from langchain_community.document_loaders import JSONLoader

loader = JSONLoader(
    file_path="./data/stu_json_lines.json",
    jq_schema=".name",
    text_content=False, # 告知JSONLoader，我抽取的内容不是字符串
    json_lines=True # 告知JSONLoader，数据是JSONLines格式
)

document = loader.load()

print(document)