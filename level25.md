# 第25关

[description](http://www.pythonchallenge.com/pc/hex/lake.html)

## 1.可获知的提示有
**`hint1`**:根据源代码中的提示：can you see the waves? 可知要用到wave模块。

把URL后缀分别改为lake1.wav，lake2.wav，…，lake25得到25个wav文件。这25个wav文件对应着原图的25块拼图。把这25个wav文件的内容依次拼接起来，会得到一张300*300大小的图片。

## 2.code
```python
##25  wave模块，图片拼接paste

import wave
import os
from PIL import Image


if __name__ == "__main__":

    #下载lake1.wav,lake2.wav,...lake25.wav
    for i in range(1,26):
        command = "curl -u butter:fly -O http://www.pythonchallenge.com/pc/hex/lake" + str(i) + ".wav"
        os.system(command)

    result = Image.new("RGB",(300,300),0)

    for i in range(1,26):
        file = "lake"+str(i)+".wav"
        data = wave.open(file,"r")
        # frames = data.getnframes()  #10800/3=3600
        bytes = data.readframes(data.getnframes())
        img = Image.frombytes(mode="RGB",size=(60,60),data=bytes) #获取一张图
        upper_left = (60*((i-1)%5),60*((i-1) // 5))
        result.paste(img,upper_left)  #将一张图粘贴到另一张图像上
    result.save("level25.png")  #decent

    ###闯关密码：decent



```
得到第26关入口: http://www.pythonchallenge.com/pc/hex/decent.html
## 3.知识点
### 3.1 img.paste(image,box)
将图image粘贴到另一张图像img的指定位置box上。变量box或者是一个给定左上角的2元组，或者是定义了左，上，右和下像素坐标的4元组，或者为空（与（0，0）一样）。如果给定4元组，被粘贴的图像的尺寸必须与区域尺寸一样。
如果模式不匹配，被粘贴的图像将被转换为当前图像的模式。








