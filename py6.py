#6.zipfile模块

import zipfile
import re

if __name__ == "__main__":

    inputPath = "D:\\pycharm\\test\\channel.zip"

    zip = zipfile.ZipFile(inputPath,'r')

    next = 90052
    comments = []

    while(True):
        cur_file = str(next) + ".txt"
        res = str(zip.read(cur_file),encoding = "utf-8")
        print("res: " , res)

        try:
            next = re.findall("[0-9]", res) #获取下一个文件名对应的数字
            next = "".join(next)
            next = int(next)
        except:
            break

        print("next: ", next)
        com = str(zip.getinfo(cur_file).comment,encoding = "utf-8")
        comments.append(com)

    #print(comments)
    end = ""
    for lists in comments:
        end += lists
    print(end)

