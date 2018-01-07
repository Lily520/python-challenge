# 第27关

[description](http://www.pythonchallenge.com/pc/hex/speedboat.html)

## 1.可获知的提示有
**`hint1`**:点击图片，提示输入用户名和密码，这一关要找到用户名和密码

**`hint2`**:根据提示得到zigzag.gif,图片上每个像素值是调色板的索引，将每一个像素替换为调色板中相应的颜色。

**`hint3`**:imdata,im_trans两者对齐，记录不同之处的坐标以及相应内容。坐标信息形成一幅图片(not key word)，不同的内容是一串压缩的字符串，解压后得到许多Python关键字。将关键字去除，求得用户名和密码。

## 2.code
```python

##27

from PIL import Image
import bz2
import keyword

if __name__ == "__main__":
    im = Image.open("zigzag.gif")
    imdata = im.tobytes()

    ## 图片上每个像素值是调色板的索引，将每一个像素替换为调色板中相应的颜色
    From = bytes([i for i in range(256)]) #
    To = im.palette.getdata()[1][::3]  #颜色调色板表格。如果图像的模式是“P”，则返回ImagePalette类的实例；否则，将为None。
    table = bytes.maketrans(From,bytes(To))
    im_trans = imdata.translate(table)

    ## imdata([1:]),im_trans([:-1])对齐，记录不同
    zipped = list(zip(imdata[1:],im_trans[:-1]))
    diff = [p for p in zipped if p[0] != p[1]] #记录不同元素
    indices = [m for m,n in enumerate(zipped) if n[0] != n[1]] #记录不同索引

    newImage = Image.new("RGB",size=im.size)
    colors = [(255,255,255)]*len(imdata)
    for i in indices:
        colors[i] = (0,0,0)
    newImage.putdata(colors)
    newImage.save("level27.png")  # not key word

    diff0 =[i[0] for i in diff]
    text = bz2.decompress(bytes(diff0))
    print(keyword.iskeyword(exec))
    result = [i.decode() for i in set(text.split()) if not keyword.iskeyword(i.decode())]
    print(result)  ##['switch', '../ring/bell.html', 'repeat', 'exec', 'print']



    #闯关密码： 用户名：repeat 密码：switch


```
得到第28关入口: http://www.pythonchallenge.com/pc/ring/bell.html
## 3.知识点
### 3.1 im.palette.getdata()
颜色调色板表格。如果图像的模式是“P”，则返回ImagePalette类的实例；否则，将为None。

### 3.2 keyword.iskeyword(str)
判断字符船是不是python关键字







