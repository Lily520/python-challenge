#实现方法2：利用正则表达式
#a = [1,11,21,1211,111221,...]

import re

if __name__ == "__main__":
    a = "1"
    for i in range(1,31):
        next = [str(len(i + j)) + str(i) for i, j in re.findall(r"(\d)(\1*)", a)]  #（first appearance,following appearance）
        a = "".join(next)
    print(len(a)) #5808