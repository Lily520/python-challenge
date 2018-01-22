# 第32关

[description](http://www.pythonchallenge.com/pc/rock/arecibo.html)

## 1.可获知的提示有
**`hint1`**:本关是一个叫 Nonogram 的游戏：(https://zh.wikipedia.org/wiki/Nonogram)

**`hint2`**:根据page source得到warmup.txt，通过解warmup.txt得到up.txt，再解up.txt得到结果。

根据最后得到的代表python的大蟒蛇，查看python.html："Free" as in "Free speech", not as in "free...

谷歌搜索，发现缺少的词是beer。

于是，得到闯关密码：beer


## 2.code
```python

# 32 Nonogram

from PIL import Image

def readData(file): #获取矩阵的大小，各行数据，各列数据
    flag = -1 #标记读取到的数据类别:dimensions，horizontal，vertical
    dimensions = [] #维度
    horizontal = [] #矩阵各行数据
    vertical = [] #矩阵各列数据
    dicts = [dimensions,horizontal,vertical]

    with open(file) as f1:
        lines = f1.readlines()
        for line in lines:
            if line != "\n":
                line = line.strip("\n").split(" ")
                if line[0] == "#":
                    flag += 1
                else:
                    dicts[flag].append(list(map(int,line)))
    f1.close()
    return dimensions[0],horizontal,vertical

def candidata(num,maxlen): #递归获得所有的备选排列,"#"为点亮
    candi = []

    for i in range(maxlen+2-sum(num)-len(num)):
        cans = 'o'*i + "#"*num[0]

        if len(num) == 1:
            tail = 'o'*(maxlen - len(cans))
            candi.append(cans+tail)
        else:
            tail = ["o" + j for j in candidata(num[1:],maxlen-len(cans)-1)]
            candi.extend([cans+j for j in tail])
    return candi


def findinit(x,y,horData,verData): #获取每一行和每一列各种可能的备选排列
    candiH = []
    candiV = []

    for i in range(y): #获取每一行的可能排列
        candiH.append(candidata(horData[i],x))
    for i in range(x):
        candiV.append(candidata(verData[i], y))
    return candiH,candiV


def check(candi,pos,value): #对某行（列）在给定位置和状态下选择不冲突的备选方案
    newcandi = []
    for i in candi:
        if i[pos] == value:
            newcandi.append(i)
    return newcandi


if __name__ == "__main__":
    # size,horData,verData = readData("warmup.txt") #返回矩阵的大小，各行数据，各列数据  处理后得到的图片是一个向上的箭头
    size,horData,verData = readData("up.txt") #处理后得到的结果是python的大蟒蛇

    candiH,candiV = findinit(size[0],size[1],horData,verData) #获取各种可能的备选排列

    result = [] #存储最终排列方式
    for i in range(size[0]):
        result.append([" " for j in range(size[1])])

    count = 0
    num = size[0] * size[1]

    while count <  num:
        for index in range(size[0]):#先针对每一行
            i = candiH[index] #index行的备选排列
            if i == "done": #index行排列已确定
                continue
            elif len(i) == 1: #index行只有一种备选排列
                for j in range(size[1]):
                    if result[index][j] == " ":
                        result[index][j] = i[0][j]
                        count += 1
                        candiV[j] = check(candiV[j],index,i[0][j])
                i = "done"
            else: #有多个备选排列
                for j in range(size[1]): #逐列筛选可能的组合
                    if result[index][j] != " ": #只考虑空闲的方格
                        continue
                    for ele in i[1:]:
                        if ele[j] != i[0][j]:
                            break
                    else:#for循环正常结束，表明所有备选排列中j列的值一致，那么此一致的值便是该方格的取值
                        result[index][j] = i[0][j]
                        count += 1
                        candiV[j] = check(candiV[j], index, i[0][j])


        for index in range(size[1]): #再针对每一列,与上面思路类似
            i = candiV[index] #index列的候选排列
            if i == "done": #index列排列已确定
                continue
            elif len(i) == 1: #只有一种备选排列
                for j in range(size[0]):
                    if result[j][index] == " ":
                        result[j][index] = i[0][j]
                        count += 1
                        candiH[j] = check(candiH[j],index,i[0][j])
                i = "done"
            else: #有多个备选排列
                for j in range(size[0]):#逐行筛选可能的组合
                    if result[j][index] != " ": #只考虑空闲的方格
                        continue
                    for ele in i[1:]:
                        if ele[j] != i[0][j]:
                            break
                    else:#for循环正常结束，表明所有备选排列中j行的值一致，那么此一致的值便是该方格的取值
                        result[j][index] = i[0][j]
                        count += 1
                        candiH[j] = check(candiH[j], index, i[0][j])


    s = []
    for i in range(size[0]):
        s.extend([1 if result[i][j] == "o" else 0 for j in range(size[1])])

    img = Image.new("1",(size[1],size[0]))
    img.putdata(s)
    img.save("level32-1.png")

    ###根据最后得到的代表python的大蟒蛇，查看python.html："Free" as in "Free speech", not as in "free...
    ##谷歌搜索，发现缺少的词是beer

    ##闯关密码：beer




```
得到第33关入口: http://www.pythonchallenge.com/pc/rock/beer.html








