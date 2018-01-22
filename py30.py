## 30 将csv文件中的像素值填充到图片中获得计算公式

from PIL import Image
import numpy as np

if __name__ == "__main__":

    length = 0  # 浮点数个数
    with open("yankeedoodle.csv","r") as f:
        content = f.read().replace("\n","").replace(" ","").split(",")
        length = len(content)
    print(length)##7367

    img_size = [x for x in range(2,length) if length % x == 0] ##要填充的图片大小
    print(img_size) #[53, 139]

    img = Image.new(mode="F",size=img_size)
    img.putdata([float(x) for x in content],256)
    img = img.transpose(Image.FLIP_LEFT_RIGHT) #图片从左向右翻转
    img = img.transpose(Image.ROTATE_90)  #图片逆时针翻转90度
    img.show()  ##得到计算公式 n=str[i][5] + str[i+1][5] + str[i+2][6]


    res = [chr(int(x[0][5] + x[1][5] + x[2][6])) for x in zip(content[0::3], content[1::3], content[2::3])]
    print("".join(res))
    #o, you found the hidden message.
    #There is lots of room here for a long message, but we only need very little space to say "look at grandpa", so the rest is just garbage.
    #VTZ.l'tf*Om@I"p]。。。。（后面省略了）

    ##闯关答案：grandpa

