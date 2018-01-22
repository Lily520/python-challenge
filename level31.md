# 第31关

[description](http://www.pythonchallenge.com/pc/ring/grandpa.html)

## 1.可获知的提示有
**`hint1`**:点击图片，提示输入用户名，密码：用户名kohsamui，密码thailand。跳到下一页面。

**`hint2`**:页面显示的是曼德布洛特集合 (Mandelbrot set) 。按照Page Source里面的参数，画出一张曼德布罗特集合的图(曼德布洛特集合全部落在复平面中半径为2的圆内)，找出画出的图和网页中的图的差异，将像素点有差异的点收集起来组成另一张图片。


[曼德布洛特集合介绍](https://msdn.microsoft.com/library/jj635753(v=vs.85))

## 2.code
```python

# 31 画曼德布罗特集合图,将与原图像素点有差异的点收集起来

from PIL import Image

if __name__ == "__main__":
    left = 0.34
    top = 0.57
    width = 0.036
    height = 0.027
    iterations = 128

    img = Image.open("mandelbrot.gif","r")
    w,h = img.size  #640 480

    xstep = width/w
    ystep = height/h

    ##画曼德布罗特集合图
    result = []
    for y in range(h-1,-1,-1):
        for x in range(w):
            c = complex(left+x*xstep,top+y*ystep)
            z = 0+0j

            for num in range(iterations):
                z = z*z+c
                if abs(z) > 2: #曼德布洛特集合全部落在复平面中半径为2的圆内
                    break
            result.append(num)
    img2 = img.copy()
    img2.putdata(result)
    # img2.show()

    diff = [(i-j) for i,j in zip(img.getdata(),img2.getdata()) if (i-j) != 0] #求两幅图的差异，差值都为16，-16
    # print(len(diff))  #1679
    new_size = [x for x in range(2,len(diff)) if len(diff) % x == 0] #将差值存入图片，求此图片尺寸大小
    # print(new_size)#[23, 73]

    #将得到的差异数据存入新的图片
    newImage = Image.new("L",new_size)
    print(diff)
    print([x > 0 and 255 or 0 for x in diff])
    newImage.putdata([x< 0 and 255 or 0 for x in diff])
    newImage.resize((230,730))
    newImage.save("31.jpg")

    ##搜索图片，得到闯关密码：arecibo





```
得到第32关入口: http://www.pythonchallenge.com/pc/rock/arecibo.html








