# 第23关

[description](http://www.pythonchallenge.com/pc/hex/bonus.html)

## 1.可获知的提示有
**`hint1`**:查看源代码：what is this module?this是python的一个模块。

**`hint2`**:源代码最下面一句话：'va gur snpr bs jung?'，此提示与第一关类似，因此仿照第一关的做法用translate。

需要通过第一关中translate函数处理第二个提示信息：通过this.py，可知字母的偏移是13位。

## 2.code
```python
#23 this，string模块

import this
import string

if __name__ == "__main__":

    input = "va gur snpr bs jung"

    From = string.ascii_lowercase
    To = string.ascii_lowercase[13:] + string.ascii_lowercase[:13]

    str = str.maketrans(From,To)

    result = input.translate(str)
    print(result) #in the face of what

    #import this 后的一句输出是：In the face of ambiguity
    ## 答案：ambiguity 



```
得到第24关入口: http://www.pythonchallenge.com/pc/hex/ambiguity.html








