# 第6关

[description](http://www.pythonchallenge.com/pc/def/channel.html)

## 1.可获知的提示有
**`hint1`**:查看网页源代码，发现单词“zip"。将链接中html换成zip，下载.zip文件。

**`hint2`**:查看解压出的readme文件:
         
    welcome to my zipped list.
    hint1: start from 90052
    hint2: answer is inside the zip

因此,本题是从90052.txt开始,通过txt里面的内容不断找到下一个txt,直到最后。
最后的文本中的信息是： Collect the comments.
因此，需要把每个文件的comment弄出来。

## 2.code
```python
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
    print(end) #hockey

```
得到链接：http://www.pythonchallenge.com/pc/def/hockey.html
打开后，得到：it's in the air. look at the letters.因此，组成hockey的字母才是重点，同时通过 in the air 暗示得到是：oxygen(氧气)
得到第七关入口: http://www.pythonchallenge.com/pc/def/oxygen.html
## 3.知识点

	* 打开zipfile文件：  导入库 zipfile
```python
import zipfile
zip = zipfile.ZipFile(inputPath,'r')
zip.read(cur_file)
```
	* 正则表达式：   re.findall()
	* zipfile文件中的文件有comment信息：   zip.getinfo(file).comment








