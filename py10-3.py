#实现方法3： 利用itertools模块的groupby函数
#a = [1,11,21,1211,111221,...]
from itertools import groupby

if __name__ == "__main__":
    a = "1"
    for i in range(1, 31):
        next = [str(len(list(all_num))) + str(num) for num, all_num in groupby(a)]
        a = "".join(next)
    print(len(a))