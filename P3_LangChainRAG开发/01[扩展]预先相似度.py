import numpy as np

def get_dot(vec_a, vec_b):
    '''计算2个向量的点积，2个向量的同纬度数字乘积之和'''
    if len(vec_a) != len(vec_b):
        raise ValueError('两个向量的维度不一致')

    dot_sum = 0
    for a, b in zip(vec_a, vec_b):
        dot_sum += a * b

    return dot_sum


def get_norm(vec):
    '''计算向量的模，即向量的每个数字的求平方再求和再开根号'''
    sum_square = 0
    for v in vec:
        sum_square += v ** 2

    # numpy sqrt完成开根号
    return np.sqrt(sum_square)

def cosine_similarity(vec_a, vec_b):
    '''计算两个向量的余弦相似度,两个向量的点积除以两个向量的摸乘积'''

    result = get_dot(vec_a, vec_b) / (get_norm(vec_a) * get_norm(vec_b))
    print(result)

if __name__ == '__main__':
    vec_a = [1, 2, 3]
    vec_b = [4, 5, 6]
    cosine_similarity(vec_a, vec_b)