# 第9关

[description](http://www.pythonchallenge.com/pc/return/good.html)

## 1.可获知的提示有
**`hint1`**:图片中有许多点，同时 'connect the dots',因此，应该是通过图像处理将点连接起来。  
**`hint2`**:查看网页源代码，有2组数据，应该是要连接的点的坐标。
因此,本题是通过图像处理模块画线。

## 2.code
```python
from PIL import Image, ImageDraw

if __name__ == "__main__":
    first = [] #太长省略，运行之前记得补全
    second = [] #太长省略，运行之前记得补全

    image = Image.open("good.jpg")
    draw = ImageDraw.Draw(image)

    # fill=(R,G,B) R,G,B的值都在0-255之间
    draw.line(first, fill=(255, 0, 0))
    draw.line(second, fill=128)
    image.show()

```
得到一头牛的轮廓。输入cow,得到：hmm. it's a male. 因此，应该是bull。
得到第10关入口: http://www.pythonchallenge.com/pc/return/bull.html
## 3.知识点
pil模块的ImageDraw模块的Draw中的line函数，用于画线。






