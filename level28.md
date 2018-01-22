# 第28关

[description](http://www.pythonchallenge.com/pc/ring/bell.html)

## 1.可获知的提示有
**`hint1`**:攻略里说RING-RING-RING，读着读着就变成了GREEN. 进入green.html，得到提示yes, green.

**`hint2`**:提取图片的G通道，相邻像素做差，将差值绝对值不为42的提取出来，得到通关信息。



## 2.code
```python
## 28 PIL,提取G通道，每相邻两列像素做差

from PIL import Image

if __name__ == "__main__":
    img = Image.open("bell.png")

    green = list(img.split()[1].getdata()) #提取G通道
    diff = [abs(i-j) for i,j in zip(green[0::2],green[1::2]) if abs(i-j) != 42]  #每相邻两列像素做差，发现差的绝对值大多为42，将不是42的保存下来
    str_diff = bytes(diff).decode() #whodunnit().split()[0] ?
    result = 'Guido van Rossum'.split(" ")[0]
    print(result) #Guido

    ##得到通关密码：guido



```
得到第29关入口: http://www.pythonchallenge.com/pc/ring/guido.html
## 3.知识点
### 3.1 green = list(img.split()[1].getdata())
提取rgb图像的g通道像素







