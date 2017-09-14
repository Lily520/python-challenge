# 第2关

[description](http://www.pythonchallenge.com/pc/def/ocr.html)

## 1.可获知的提示有
**`hint1`**:查看网页源代码  

**`hint2`**:find rare characters in the mess below. 

因此  ，本题是求出现次数最少的字符。

## 2.code
```python
#2.找到一段字符串中出现次数最少的字符

if __name__ == "__main__":
    #input = "...." #太长省略,运行前要先替换成原网页中的字符串
    dicts = {}
    for ele in input:
        dicts.setdefault(ele,0)
        dicts[ele] += 1

    min_times = min(dicts.items(),key=lambda x:x[1])[1] #求字典对应的最小值
    print(type(min_times))
    print(min_times)
    for k in dicts.keys():
        if dicts[k] == min_times:
            print(k,dicts[k])  #得到出现次数最少的字符连起来为：equality
```
得到第三关入口: http://www.pythonchallenge.com/pc/def/equality.html

## 3.知识点

	* 字典中不存的键，为此键设置默认值 ：   dicts.setdefault(ele,0)
	* 求字典对应的最小值：   min(dicts.items(),key=lambda x:x[1])[1]
	* 求字典最小值对应的键:  min(dicts.items(),key=lambda x:x[1])[0]
	* min(dicts.items(),key=lambda x:x[1]) 得到的结果类型为 tuple








