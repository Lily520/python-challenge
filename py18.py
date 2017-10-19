import gzip
import difflib


if __name__ == "__main__":
    content = gzip.open("deltas.gz",'rb').readlines()
    data1 = []
    data2 = []
    for line in content: #将左右两列数据分别存放在data1,data2
        data1.append(line[0:53].decode()+"\n")
        data2.append(line[56:].decode())


    str_diff = list(difflib.Differ().compare(data1,data2)) #做对比

    f1 = open("1.png",'wb')
    f2 = open("2.png","wb")
    f3 = open("3.png","wb")

    for ele in str_diff:
        wri_ele = bytes([int(i,16) for i in ele[2:].strip().split(" ") if i])
        print(wri_ele)
        if ele[0] == "+":
            f1.write(wri_ele)
        elif ele[0] == "-":
            f2.write(wri_ele)
        else:
            f3.write(wri_ele)

    f1.close() #butter
    f2.close() #fly
    f3.close() #../hex/bin.html

