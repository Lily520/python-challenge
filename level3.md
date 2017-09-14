# 第2关

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
得到第三关入口: http://www.pythonchallenge.com/pc/def/equality.html

## 3.知识点

	* 字典中不存的键，为此键设置默认值 ：   dicts.setdefault(ele,0)
	* 求字典对应的最小值：   min(dicts.items(),key=lambda x:x[1])[1]
	* 求字典最小值对应的键:  min(dicts.items(),key=lambda x:x[1])[0]
	* min(dicts.items(),key=lambda x:x[1]) 得到的结果类型为 tuple








