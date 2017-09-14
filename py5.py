import pickle

if __name__ == "__main__":

    input = open("banner.p",'rb')
    data = pickle.load(input) #反序列化
    #print(data)
    str = ""
    for list in data:
        print(list)
        for i in list:
            print("1: ",i[0],i[1]) #i[0]为字符，i[1]为字符个数
            print("2: ",i[0]*i[1])# 将i[0]重复i[1]次
            str += i[0]*i[1]
            #print("str: ", str)
        str += "\n"
print(str)