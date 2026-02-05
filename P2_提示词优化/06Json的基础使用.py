import json

d = {
    "name": "周杰轮",
    "age": 11,
    "gender": "男"
}

# 字典转换为JSON字符串
s = json.dumps(d, ensure_ascii=False)
print(s)

l = [
    {
        "name": "周杰轮",
        "age": 11,
        "gender": "男"
    },
    {
        "name": "蔡依林",
        "age": 16,
        "gender": "女"
    },
    {
        "name": "李小鹏",
        "age": 12,
        "gender": "男"
    }
]
print(json.dumps(l, ensure_ascii=False))

json_str = '{"name": "周杰轮", "age": 11, "gender": "男"}'
json_array_str = ('[{"name": "周杰轮", "age": 11, "gender": "男"}, '
                  '{"name": "蔡依林", "age": 16, "gender": "女"}, '
                  '{"name": "李小鹏", "age": 12, "gender": "男"}]')

# JSON字符串转换为字典
res_dict = json.loads(json_str)
print(res_dict, type(res_dict))

# JSON字符串转换为列表
res_list = json.loads(json_array_str)
print(res_list, type(res_list))

