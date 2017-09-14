# 第3关

[description](http://www.pythonchallenge.com/pc/def/equality.html)

## 1.可获知的提示有
**`hint1`**:查看网页源代码  

**`hint2`**:One small letter, surrounded by <b>EXACTLY</b> three big bodyguards on each of its sides.

因此,本题是求两边都被3个大写字母包围的小写字母。

## 2.code
```python
#3.正则表达式

import re
str = "" #太长省略，运行前要先替换成原网页中的字符串
s = re.findall('[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}',str) #一个小写字母两边恰被3个大写字母包围
result = [x[4] for x in s]
print(result) #linkedlist

```
得到第四关入口: http://www.pythonchallenge.com/pc/def/linkedlist.html

## 3.知识点
正则表达式的相关知识






