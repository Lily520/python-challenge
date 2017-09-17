from PIL import Image
im = Image.open("wire.png")
# print(list(im.getdata())) #(10000, 1)
data = im.getdata()

#将10000*1的图片按螺旋形状重新排列成100*100

directions = [(1,0),(0,1),(-1,0),(0,-1)]  #定义前进方向
steps = 100

new_im = Image.new(im.mode,(100,100))
count = 0
x_initial = 0
y_initial = 0

while count != 10000:

    #down (1,0) 向下
    x_down = [m for m in range(x_initial,x_initial+steps,directions[0][0])]
    y_down = [y_initial]*steps
    for (x,y) in zip(x_down,y_down):
        new_im.putpixel((x,y),data[count])
        count += 1

    #right (0,1)  向右
    steps -= 1
    x_right = [x_down[-1]]*steps
    y_right = [n for n in range(y_initial,y_initial+steps,directions[1][1])]
    for (x,y) in zip(x_right,y_right):
        new_im.putpixel((x, y), data[count])
        count += 1

    #up  向上
    x_up = [m for m in range(x_right[-1],x_initial,directions[2][0])]
    y_up = [y_right[-1]]*steps

    for (x,y) in zip(x_up,y_up):
        new_im.putpixel((x, y), data[count])
        count += 1

    #left  向左
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

