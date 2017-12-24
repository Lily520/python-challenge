from PIL import Image,ImageSequence

if __name__ == "__main__":
    im = Image.open("white.gif")
    coords = []
    for frame in ImageSequence.Iterator(im):  #遍历动态图，发现每一帧都有一个值为8的像素点
        idata = list(frame.getdata()) #像素值
        idx = idata.index(8)
        x = idx % 200
        y = idx // 200
        coords.append([x,y]) ##像素值为8的点的坐标，其中共有5组(x,y) =（100，100）

    im_new = Image.new(im.mode,im.size)
    pos = (30,30)
    letter = 1

    for p in coords:
        if p == [100,100]:#若坐标为（100，100），更改一下坐标位置，防止5个图案重叠在一起
            letter += 1
            pos = (letter*30,letter*30)
        else: #坐标不为（100，100）时，画图
            pos = (pos[0]+p[0]-100,pos[1]+p[1]-100)
            im_new.putpixel(pos,255)
    im_new.save("result.gif")
    im_new.show() #bonus
