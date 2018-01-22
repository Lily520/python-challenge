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