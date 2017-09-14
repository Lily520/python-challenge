#1. 字符串映射

import string

if __name__ == "__main__":

    trans_str = str.maketrans(string.ascii_lowercase[:],string.ascii_lowercase[2:] + string.ascii_lowercase[0:2]) #得到映射关系
    res = "map".translate(trans_str)
    print(res)   # ocr




