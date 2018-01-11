# 第29关

[description](http://www.pythonchallenge.com/pc/ring/guido.html)

## 1.可获知的提示有
**`hint1`**:

**`hint2`**:

因此,本题是求。

## 2.code
```python
##29 空格个数转为ASCII,bz2解压

from urllib.request import Request,urlopen
import bz2
import base64

if __name__ == "__main__":
    html = Request("http://www.pythonchallenge.com/pc/ring/guido.html")
    html.add_header('Authorization', 'Basic %s' % base64.b64encode(b'repeat:switch').decode())
    pageContent = urlopen(html).read().decode()
    spaces = pageContent.split("\n")[12:]  #只保留空格
    asc = bytes([(len(i)) for i in spaces]) #将每行空格个数求和并转换成ASCII
    result = bz2.decompress(asc)
    print(result) #b"Isn't it clear? I am yankeedoodle!"

    ##闯关密码：yankeedoodle



```
得到第30关入口: http://www.pythonchallenge.com/pc/ring/yankeedoodle.html
## 3.知识点
### 3.1 爬取网页内容
```python

from urllib.request import Request,urlopen
import base64

html = Request("http://www.pythonchallenge.com/pc/ring/guido.html")
html.add_header('Authorization', 'Basic %s' % base64.b64encode(b'repeat:switch').decode())
pageContent = urlopen(html).read().

```






