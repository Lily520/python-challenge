##26 MD5校验

import hashlib


if __name__ == "__main__":
    md5code = "bbb8b499a0eef99b52c7f13f4e78c24b"
    data = open("maze/mybroken.zip","rb").read()
    flag = 0

    for i in range(len(data)):
        for j in range(256):
            newData = data[:i] + bytes([j]) + data[i+1:]
            if hashlib.md5(newData).hexdigest() == md5code:
                open("repair.zip","wb").write(newData)
                print(i,j)
                flag = 1
                break
        if flag == 1:
            break



    #闯关密码：speedboat

