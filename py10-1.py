#实现方法1
# a = [1,11,21,1211,111221,...]


def getNext(num):
        str_num = str(num)
        res = ""
        lens = len(str_num)

        if lens == 1:
            res = str(1) + str_num
            return res
        else:
            start_index = 0
            count = 1
            for next_index in range(1, lens):
                if str_num[next_index] == str_num[start_index]:
                    count += 1
                else:
                    res += str(count) + str_num[start_index]
                    count = 1
                    start_index = next_index
            res += str(count) + str_num[start_index]
            return res

if __name__ == "__main__":
    a = 1
    for i in range(0, 30):
        next_a = getNext(a)
        a = next_a

    print(len(str(a)))  # 5808