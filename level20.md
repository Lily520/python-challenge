# 第20关

[description](http://www.pythonchallenge.com/pc/hex/unreal.jpg)

本题通过不断改变Range的值来求解，最终获得21关所需要的压缩文件。

## 2.code
```python
import base64
import requests

#获取当前base的网页信息
def get_range(base,limit):
    headers = {'Authorization': 'Basic ' + base64.b64encode(b'butter:fly').decode(), 'Range': 'bytes=%s-%s' % (base, limit)}
    a = requests.get("http://www.pythonchallenge.com/pc/hex/unreal.jpg", headers=headers)
    return a

#不断获取下一个base
def next_base():
    base = 30203
    limit = 2123456789
    content = []
    bases = []

    while isinstance(base,int): #base为int型
        result = get_range(base, limit)
        content.append(result.content)
        bases.append(base)
        try:
            next_base = int(result.headers['Content-Range'].split("/")[0].split("-")[1]) + 1
        except:
            next_base = "ERROR"
        base = next_base
    print(content) ## [b"Why don't you respect my privacy?\n", b'we can go on in this way for really long time.\n', b'stop this!\n', b'invader! invader!\n', b'ok, invader. you are inside now. \n', b'']
    print(bases) #[30203, 30237, 30284, 30295, 30313, 30347]

    result2 = get_range(limit,"")
    print(result2.content) #b'esrever ni emankcin wen ruoy si drowssap eht\n'
    print(result2.headers['Content-Range']) #bytes 2123456744-2123456788/2123456789

    result3 = get_range(2123456743, "")
    print(result3.content) # b'and it is hiding at 1152983631.\n'
    result4 = get_range(1152983631, "")
    result5 = result4.content
    open("unreal.zip","wb").write(result5)  #用redavni作为密码解压压缩包，便得到了21关需要处理的压缩包

if __name__ == "__main__":
    next_base()


```







