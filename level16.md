# 第16关

[description](http://www.pythonchallenge.com/pc/return/mozart.html)

## 1.可获知的提示有
**`hint1`**:let me get this straight

**`hint2`**:图片中有许多粉色线条

因此,本题有可能把这些线条弄成线就可以了。

## 2.code
```python
from PIL import Image
import numpy as np

if __name__ == "__main__":


    img = Image.open("mozart.gif")
    width, height = img.size

    # 根据图mozart知，若粉色在每行都出现，则（出现次数）% height==0
    hist = img.histogram()
    pink = [(num, hist.index(num)) for num in hist if (num % height == 0 and num != 0)]  # (出现次数,像素)

    data = img.getdata()
    data = np.array(data).reshape((height, width))
    print(data.shape)
    shiftData = np.array(
        [np.roll(data[row, :], -data[row, :].tolist().index(pink[0][1])) for row in range(height)])  # 将pink颜色移到前面
    shiftData.shape = (height * width,)  # 根据提示: let me get this straight
    print(shiftData.shape)
    img.putdata(shiftData)
    img.show() #romance


```
得到第17关入口: http://www.pythonchallenge.com/pc/return/romance.html  

## 3. 知识点
### 3.1. 求list中出现次数最多的元素
```python
     from collections import Counter
     a = Counter(list)
     a.most_common(num)#获取出现次数最多的num个字符，返回为列表，列表的每个元素为元组（出现最多次的字符，出现次数）
```

### 3.2. 计算一幅图片中出现次数最多的像素
```python
     img = Image.open("picture.gif")

     #方法一
     data = list(img.getdata())
     a = Counter(data) 
     re = a.most_common(1)
     
     #方法二
     hist = img.histogram() #返回一个图像的直方图，这个直方图是关于像素数量的list
     re = max(enumerate(hist),key=lambda x:x[1]) #返回元组：（出现次数最多的像素，出现次数）
```

### 3.3. np.where()有两种用法
     np.where(conditions,x,y) #if conditions成立，数组变为x;否则，就变为y'
     np.where(conditions) #给出数组下标

### 3.4. img.histogram()与img.getdata()的区别
     histogram：返回一个图像的直方图，这个直方图是关于像素数量的list
     getdata:返回图像像素值
### 3.5. width,height = img.size 
    #size返回的数值分别为图像的宽，高
### 3.6. 循环移位函数 
    np.roll(x,2) #向右循环移动2位






