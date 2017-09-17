# 第10关

[description](http://www.pythonchallenge.com/pc/return/bull.html)

## 1.可获知的提示有
**`hint1`**:图下方提示“len(a[30])=?",应该是求a,从而能知道a[30]的长度。  

**`hint2`**:打开网页源代码，发现有"sequence.txt"文件，打开发现：a = [1, 11, 21, 1211, 111221, 

因此,本题要通过探索规律找到a[30],从而求出长度。

## 2.code
### 2.1.实现方法1
```python
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

```
### 2.2.实现方法2:利用正则表达式
```python
#实现方法2： 利用正则表达式
#a = [1,11,21,1211,111221,...]

import re

if __name__ == "__main__":
    a = "1"
    for i in range(1,31):
        next = [str(len(i + j)) + str(i) for i, j in re.findall(r"(\d)(\1*)", a)]  #（first appearance,following appearance）
        a = "".join(next)
    print(len(a)) #5808

```
### 2.3.实现方法3:利用itertools模块的groupby函数
```python
#实现方法3： 利用itertools模块的groupby函数
#a = [1,11,21,1211,111221,...]
from itertools import groupby

if __name__ == "__main__":
    a = "1"
    for i in range(1, 31):
        next = [str(len(list(all_num))) + str(num) for num, all_num in groupby(a)]
        a = "".join(next)
    print(len(a)) #5808



```
得到第11关入口: http://www.pythonchallenge.com/pc/return/5808.html  
## 3.知识点
### 3.1.利用正则表达式，求数字连续出现的个数  
  r"(\d)(\1*)" : ()用来分组，并可以使用后向引用"\\1" "\\2" 等来引用第一个括号、第二个括号的内容。

### 3.2.tertools模块的groupby函数  
  它返回的结果是(num, all appearance), 它把相邻的重复元素挑出来放在一起




