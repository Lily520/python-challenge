# 第1关

[description](http://www.pythonchallenge.com/pc/def/map.html)

## 1.可获知的提示有
**`hint1`**:everybody thinks twice before solving this.  

**`hint2`**:图中笔记本上显示的：K->M O->Q E->G  

由hint2可知本题是求一个映射，同时K／O／E 映射到 M／Q／G都是将字符平移向后映射了两位以及hint1中的“twice”，则本题便是求字符“map”向后映射两位后得到的字符。  

## 2.code
```python
#1. 字符串映射


import string

if __name__ == "__main__":

    trans_str = str.maketrans(string.ascii_lowercase[:],string.ascii_lowercase[2:] + string.ascii_lowercase[0:2]) #得到映射关系
    res = "map".translate(trans_str)
    print(res)   # ocr
```
得到第二关入口：http://www.pythonchallenge.com/pc/def/ocr.html


## 3.知识点

### 3.1 字符串的映射

字符串的映射包含两个函数：maketrans()和translate(), 它们都在str模块中。  
str.maketrans(from,to): 该函数将from中的字符映射到to中对应位置的字符上。所以，from与to的长度应一致。  
ori_str.translate(to,del):该函数将ori_str字符串按maketrans()定义的映射关系进行映射。同时，将del中有的字符删掉。  

### 3.2 按序获取所有小写字母
```python
import string

low_str = string.ascii_lowercase #low_str即是所求所有小写字母
```





