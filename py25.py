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


