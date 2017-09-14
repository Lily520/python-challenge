#2.找到一段字符串中出现次数最少的字符


if __name__ == "__main__":
    #input = "...." #太长省略,运行前要先替换成原网页中的字符串
    dicts = {}
    for ele in input:
        dicts.setdefault(ele,0)
        dicts[ele] += 1

    min_times = min(dicts.items(),key=lambda x:x[1])[1] #求字典对应的最小值
    print(type(min_times))
    print(min_times)
    for k in dicts.keys():
        if dicts[k] == min_times:
            print(k,dicts[k])
