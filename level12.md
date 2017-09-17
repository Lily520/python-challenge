# 第12关

[description](http://www.pythonchallenge.com/pc/return/evil.html)

## 1.可获知的提示有
**`hint1`**:图中人将扑克分成了5份。  

**`hint2`**:查看网页源代码，得到evil1.jpg。在地址栏中将evil1改成evil2,按提示将.jpg改成.gfx。

因此,本题是将.gfx文件拆分成5份。

## 2.code
```python
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import numpy as np

if __name__ == "__main__":
    
    with open("evil2.gfx","rb") as f1:
        data = f1.read()
    # print(data)
    
    for i in range(5):
        open(str(i)+".jpg",'wb').write(data[i::5])
    
    #显示图片
    Image.open("0.jpg",'r').show() #dis
    Image.open("1.jpg",'r').show() #pro
    Image.open("2.jpg",'r').show() #port
    Image.open("3.jpg",'r').show() #ional
    Image.open("4.jpg",'r').show() #划掉的ity

    # solution: disproportional

```
得到第13关入口: http://www.pythonchallenge.com/pc/return/disproportional.html  
## 3.遇到的问题
显示图片3.jpg时报错：
     OSError: image file is truncated

解决办法：
在程序开头加上：
```python
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
```






