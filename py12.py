from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import numpy as np

if __name__ == "__main__":

    with open("evil2.gfx","rb") as f1:
        data = f1.read()

    for i in range(5):
        open(str(i)+".jpg",'wb').write(data[i::5])

    #显示图片
    Image.open("0.jpg",'r').show() #dis
    Image.open("1.jpg",'r').show() #pro
    Image.open("2.jpg",'r').show() #port
    Image.open("3.jpg",'r').show() #ional
    Image.open("4.jpg",'r').show() #划掉的ity

    # solution: disproportional