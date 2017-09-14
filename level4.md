# 第4关

跳转到链接 http://www.pythonchallenge.com/pc/def/linkedlist.html 后，提示将html换成php

[description](http://www.pythonchallenge.com/pc/def/linkedlist.php)

## 1.可获知的提示有
**`hint1`**:点击图片，跳转：and the next nothing is 44827，同时跳转到链接http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345

**`hint2`**:查看网页源代码：urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough.

因此,本题是不断改变nothing=后面的数字。

## 2.code
```python
#4 网络爬虫

import urllib.request

if __name__ == "__main__":
    src = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345") #初始url

    nexturl = None
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

    count = 0
    while True:
        lines = str(src.read())
        print(lines)
        splits = lines.strip("\'").strip("\n").split(" ")
        print(splits[-1]) #splits[-1]是获取到的下一个nothing=后面的数字
        try:
            nextid = int(splits[-1])
        except:
            break
        nexturl = url + str(nextid) #下一个url
        count += 1
        print(count, "::: ", nexturl)
        src.close()
        src = urllib.request.urlopen(nexturl)

```
最后几行的输出结果为：  
b'and the next nothing is 16044'  
16044  
85 :::  http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=16044  
b'Yes. Divide by two and keep going.'  
going.  

(16044/2)=8022  
因此，我们将```if __name__ == "__main__"```的下一句的链接换成：    
```src = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022")```  

再次运行，最后1行的输出为：  
b'peak.html'    
得到第五关入口: http://www.pythonchallenge.com/pc/def/peak.html  

## 3.知识点
* 爬虫库：  python3中要用urllib.request  
* 打开网页： src =  urllib.request.urlopen("url")  
* 读取网页内容： src.readline()   src.read()






