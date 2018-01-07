# 第26关

[description](http://www.pythonchallenge.com/pc/hex/decent.html)

## 1.可获知的提示有
**`hint1`**:查看page source:you've got his e-mail.根据攻略提示：发邮件给此email(leopold.moz@pythonchallenge.com,19关得到的)，得到回信：

> From: leopold.moz@pythonchallenge.com  
> Subject: Re: sorry
> Date: 2007-05-17 15:37:07 BDT

> Never mind that.

> Have you found my broken zip?

> md5: bbb8b499a0eef99b52c7f13f4e78c24b

> Can you believe what one mistake can lead to?

**`hint2`**:根据回信提示，发现24关得到的mybroken.zip无法解压，用MD5码校验恢复。

**`hint3`**:修复后解压得到speed,在根据提示：Hurry, up, I’m missing the boat。得到闯关密码speedboat

## 2.code
```python
##26 MD5校验

import hashlib


if __name__ == "__main__":
    md5code = "bbb8b499a0eef99b52c7f13f4e78c24b"
    data = open("maze/mybroken.zip","rb").read()
    flag = 0

    for i in range(len(data)):
        for j in range(256):
            newData = data[:i] + bytes([j]) + data[i+1:]
            if hashlib.md5(newData).hexdigest() == md5code:
                open("repair.zip","wb").write(newData)
                print(i,j)
                flag = 1
                break
        if flag == 1:
            break



    #闯关密码：speedboat





```
得到第27关入口: http://www.pythonchallenge.com/pc/hex/speedboat.html
## 3.知识点
### 3.1 MD5码校验
hashlib.md5(newData).hexdigest()









