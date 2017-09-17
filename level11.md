# 第11关

[description](http://www.pythonchallenge.com/pc/return/5808.html)

## 1.可获知的提示有
**`hint1`**:图片title为：odd even。

**`hint2`**:图片看上去好像是几幅图的叠加。

因此,本题是将图片按奇偶像素进行分割。

## 2.code
```python

#11  图像奇偶像素的拆分

from PIL import Image

if __name__ == "__main__":

    img = Image.open("cave.jpg")
    width, height = img.size

    odd = Image.new(img.mode,(width//2,height//2)) #奇数
    even = Image.new(img.mode,(width//2,height//2)) #偶数

    for w in range(width):
        for h in range(height):
            get_color = img.getpixel((w,h))

            if (w+h) % 2 == 0:
                even.putpixel((w//2,h//2),get_color)
            else:
                odd.putpixel((w//2,h//2),get_color)

    # even.show() #evil
    odd.show()


```
得到第12关入口: http://www.pythonchallenge.com/pc/return/evil.html  

## 3.知识点
1. Image.new(mode,(x,y))  新建大小为（x,y）的图片,模式为mode,例如“RGB”  
2. img.getpixel((X,Y))  获取图片img在（X,Y）处的像素值  
3. img.putpixel((w,h),color) 将图片(w,h)像素点的像素值设置为color  






