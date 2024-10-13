import random
import xxhash
import numpy as np
import base64
import os

from mypy.util import hash_digest

def calculate_xxh32_digest(filename):
    # 将文件名编码为 UTF-8 字节串
    utf8_filename = filename.encode('utf-8')
    # 使用 xxh32_intdigest 函数计算出文件名 UTF-8 字节串的哈希值
    hash_value = xxhash.xxh32_intdigest(utf8_filename)
    return hash_value

def generate_mersenne_twister_random_bytes(seed, length):
    # 初始化 Mersenne Twister 随机数生成器
    np.random.seed(seed)
    # 生成指定长度的随机字节串
    random_bytes = np.random.bytes(length)
    return random_bytes


def main():
    # 假设你的文件名是 'example.zip'
    filename = input('请输入文件名: ')

    # 步骤 1: 计算文件名的 xxh32 哈希值
    seed = calculate_xxh32_digest(filename)

    # 步骤 2: 使用 Mersenne Twister 算法生成随机字节串
    # 长度为 3*20/4 = 15 字节（因为 Base64 编码后长度为 20 字符）
    random_bytes = generate_mersenne_twister_random_bytes(seed, 15)

    # 步骤 3: 将生成的随机字节串使用 Base64 编码
    encoded_bytes = base64.b64encode(random_bytes)
    # 去掉 Base64 编码字符串中的换行符（如果有的话）
    password = encoded_bytes.decode('utf-8').strip()

    # 确保密码长度为 20 字符，如果不是则截断或填充（这里应该是 20 字符因为我们是按 20 字符长度计算的）
    # 但由于我们直接计算了长度，这一步通常是多余的，除非有特殊的 Base64 实现或要求
    assert len(password) == 20, f"Generated password length is not 20: {len(password)}"

    print(f"解压密码是: {password}")


if __name__ == "__main__":
    main()
