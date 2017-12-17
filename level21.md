# 第21关

这一关并未给出网址，而是处理20关得到的压缩文件，得到通关密码。

## 1.可获知的提示有

解压得到的readme 文件：
Yes! This is really level 21 in here. 
And yes, After you solve it, you'll be in level 22!

Now for the level:

* We used to play this game when we were kids
* When I had no idea what to do, I looked backwards.


这一关我们要对package.pack进行bz2解压，zlib解压和反转操作，不同的操作用不同的字符进行记录。

## 2.code
```python
import zlib
import bz2

import sys
# sys.setdefaultencoding()
# sys.setdefaultencoding('utf-8')

def decompresses(path):
    s = open(path,'rb').read()
    print(s)
    zh = b'x\x9c'
    bh = b'BZ'

    logs = []
    while True:
        sh = s[:2]
        if sh == zh: ##zlib
            s = zlib.decompress(s)
            logs.append(" ")
        elif sh ==bh: ##bz2
            s = bz2.decompress(s)
            logs.append("#")
        elif s[-1:-3:-1] in [zh,bh]:
            print(s[-1:-3:-1])
            s = s[::-1] ##反转
            logs.append("\n")
        else:
            break
    print("".join(logs)) #copper


if __name__ == "__main__":
    path = "/Users/zzz/Documents/pycharm/challenge/unreal/package.pack"
    decompresses(path)




```
得到第22关入口: http://www.pythonchallenge.com/pc/hex/copper.html






