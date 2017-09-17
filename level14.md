# 第14关

[description](http://www.pythonchallenge.com/pc/return/italy.html)

## 1.可获知的提示有  
**`hint1`**:大图下面有个100*100的小图。通过求解，发现小图是10000*1的，因此，图片被reshape了。  

**`hint2`**:螺旋状的面包。表明我们可能需要按螺旋形状将10000*1的图reshape成100*100的。  

因此,本题是将图片重新按螺旋形状排列。  

## 2.code
```python

from PIL import Image
im = Image.open("wire.png")
# print(list(im.getdata())) #(10000, 1)
data = im.getdata()

#将10000*1的图片按螺旋形状重新排列成100*100

directions = [(1,0),(0,1),(-1,0),(0,-1)] #定义前进方向
steps = 100

new_im = Image.new(im.mode,(100,100))
count = 0
x_initial = 0
y_initial = 0

while count != 10000:

    #down (1,0) #向下
    x_down = [m for m in range(x_initial,x_initial+steps,directions[0][0])]
    y_down = [y_initial]*steps
    for (x,y) in zip(x_down,y_down):
        new_im.putpixel((x,y),data[count])
        count += 1

    #right (0,1) #向右
    steps -= 1
    x_right = [x_down[-1]]*steps
    y_right = [n for n in range(y_initial,y_initial+steps,directions[1][1])]
    for (x,y) in zip(x_right,y_right):
        new_im.putpixel((x, y), data[count])
        count += 1

    #up 向上
    x_up = [m for m in range(x_right[-1],x_initial,directions[2][0])]
    y_up = [y_right[-1]]*steps

    for (x,y) in zip(x_up,y_up):
        new_im.putpixel((x, y), data[count])
        count += 1

    #left  向左
    steps -= 1
    if steps > 0 :
        x_left = [x_up[-1]]*steps
        y_left = [n for n in range(y_up[-1],y_initial,directions[3][1])]
        for (x,y) in zip(x_left,y_left):
            new_im.putpixel((x, y), data[count])
            count += 1

        x_initial = x_left[-1]
        y_initial = y_left[-1]
        # print("count:" ,count)

new_im.show()


```
得到一张猫的图片。输入cat跳到下一个网页：and its name is uzi. you'll hear from him later. 

得到第15关入口: http://www.pythonchallenge.com/pc/return/uzi.html







