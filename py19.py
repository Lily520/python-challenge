import base64
import wave

# ##1. 利用base64生成wav文件，结果文件语音为：sorry
with open("19.txt",'rb') as input, open("indian.wav","wb") as output:
    base64.decode(input,output)


##2. 根据提示音，跳转到...sorry.html页面，只得到：- "what are you apologizing for?"
## 根据Page Source里的提示：Maybe my computer is out of order.
## 同时地图中海洋和陆地颜色标反了。
## 因此，我们将音频中的每一帧进行颠倒

#2.将每一帧反转
inWave = wave.open("indian.wav","r")
outWave = wave.open("indian2.wav","w")
outWave.setnchannels(inWave.getnchannels())
outWave.setframerate(inWave.getframerate()//2)
outWave.setsampwidth(inWave.getsampwidth())
outWave.writeframes(inWave.readframes(inWave.getnframes())[::2])

