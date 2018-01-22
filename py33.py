# 33 去除图片中最亮像素

from PIL import Image
import numpy as np

if __name__ == "__main__":
    img = Image.open("beer2.png")
    data = list(img.getdata())

    for num in range(254,-1,-1):
        data = [i for i in data if i < num]  # 去除不小于num的像素值
        w = int(np.sqrt(len(data)))  # 新建图片的长和宽
        if w*w == len(data) and w > 0:  #使剩下的像素点的个数为平方数(fair and square)
            new = Image.new(mode=img.mode,size=(w,w))
            new.putdata(data)
            new.save("img/"+str(w)+'.png')

    ##得到好多个字母，外边有方框的字母组成 gremlins


