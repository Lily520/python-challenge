# 第8关

[description](http://www.pythonchallenge.com/pc/def/integrity.html)

## 1.可获知的提示有
**`hint1`**: working hard => busy, 因此要用到bz2模块。  

**`hint2`**:查看网页源代码，看到最后有两串字符串。  

因此,本题是用bz2模块解压两个字符串。

## 2.code
```python
import bz2

if __name__ == "__main__":
    un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

    user = bz2.decompress(un)
    pwr = bz2.decompress(pw)
    print(user) #b'huge'
    print(pwr) #b'file'

```
点击图片，输入用户名，密码。  
得到第九关入口: http://www.pythonchallenge.com/pc/return/good.html
## 3.知识点  
1.压缩模块 bz2






