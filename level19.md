# 第19关

[description](http://www.pythonchallenge.com/pc/hex/bin.html)  
账号：butter  密码：fly

## 1.解题过程

### 1.1 将字符串利用base64生成wav文件
```python
with open("19.txt",'rb') as input, open("indian.wav","wb") as output:
    base64.decode(input,output)
```

结果文件语音为：sorry

### 1.2 根据提示音，跳转到sorry页面，只得到：- "what are you apologizing for?"
  根据Page Source里的提示：Maybe my computer is out of order.
  同时地图中海洋和陆地颜色标反了。
  因此，我们将音频中的每一帧进行颠倒。
  
  ```python
inWave = wave.open("indian.wav","r")
outWave = wave.open("indian2.wav","w")
outWave.setnchannels(inWave.getnchannels())
outWave.setframerate(inWave.getframerate()//2)
outWave.setsampwidth(inWave.getsampwidth())
outWave.writeframes(inWave.readframes(inWave.getnframes())[::2])
  ```

### 1.3 从indian2.wav听出： you are a idiot.
跳转到idiot,得到第20关入口: http://www.pythonchallenge.com/pc/hex/idiot2.html

## 2.code
```python
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

```

## 3.知识点
### 3.1 wave模块的相关函数
getnchannels(): 返回 audio channel 数目
getsampwidth(): 返回采样宽度，以byte为单位
getframerate(): 返回采样频率
getnframes(): 返回音频帧数
getparams(): 返回一个tuple,(nchannels,sampwidth,frametare,nframes,comptype,compname)
getcomptype(): 返回压缩类型

### 3.2 生成音频

```python
# 利用base64生成wav文件
with open("19.txt",'rb') as input, open("indian.wav","wb") as output:
    base64.decode(input,output)
```
### 3.3 反转音频的每一帧

#### 3.3.1 方法一
```python
#将每一帧反转
inWave = wave.open("indian.wav","r")
outWave = wave.open("indian2.wav","w")
outWave.setnchannels(inWave.getnchannels())
outWave.setframerate(inWave.getframerate()//2)
outWave.setsampwidth(inWave.getsampwidth())
outWave.writeframes(inWave.readframes(inWave.getnframes())[::2])

```

#### 3.3.2 方法二
```python
inWave = wave.open("indian.wav","r")
outWave = wave.open("indian4.wav","w")
outWave.setnchannels(inWave.getnchannels())
outWave.setframerate(inWave.getframerate()*2)
outWave.setsampwidth(inWave.getsampwidth()//2)
outWave.big_endiana = 1
outWave.writeframes(inWave.readframes(inWave.getnframes()))
```







