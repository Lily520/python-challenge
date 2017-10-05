# 第18关

[description](http://www.pythonchallenge.com/pc/return/balloons.html)

## 1.解题思路
1. 打开网页，标题为：can you tell the difference?   
我们发现，两幅图的区别只是亮度不同。将链接改为brightness。网页显示并无改变，查看网页源代码，得到：maybe consider deltas.gz 
2. 下载deltas.gz： http://www.pythonchallenge.com/pc/return/deltas.gz
用gzip查看压缩文件，有两组16进制数  
3. 根据1中的提示，用difflib将两组数做比较。得到的结果有3种类型：以“+ ”开头，以“- ”开头，以“  ”开头。将3种类型的结果分别存放，并在图片中显示出来。    
图片中显示的信息，便可得到闯关信息。

## 2.code
```python
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

```
得到第19关入口: http://www.pythonchallenge.com/pc/hex/bin.html  账号：butter 密码：fly  
## 3.知识点
### 3.1 gzip解压缩模块
gzip.open("deltas.gz",'rb')： 可以打开读取压缩文件，并可用于读取内容

### 3.2 difflib模块
difflib.Differ().compare(data1,data2)：  
用于比较data1,data2的差异。得到的结果共有三种类型：以“+ ”开头，以“- ”开头，以“  ”开头。   
其中，“+ ”开头的表示：只在data1中出现；  
“- ” 开头的表示：只在data2中出现；  
“  ”开头的表示：在data1和data2中共同出现。






