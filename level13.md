# 第13关

[description](http://www.pythonchallenge.com/pc/return/disproportional.html)

## 1.可获知的提示有
**`hint1`**:第12关中，将evil1依次替换成evil2,evil3,evil4,evil4.jpg无法打开。因此，   
用curl -u命令打开: curl -u huge:file http://www.pythonchallenge.com/pc/return/evil4.jpg     
得到：Bert is evil! go back!

**`hint2`**: 图片下方显示：phone that evil。

**`hint3`**:点击数字5，得到一个xml文件。

因此,本题是用xmlrpc解析xml文件，然后用phone方法返回evil对应的结果。


## 2.code
```python

import xmlrpc.client

if __name__ == "__main__":

    php_html = "http://www.pythonchallenge.com//pc//phonebook.php"
    re_ans1 = xmlrpc.client.ServerProxy(php_html)
    
    #['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']
    print(re_ans1.system.listMethods())
    print(re_ans1.system.methodHelp("phone")) #Returns the phone of a person
    print(re_ans1.system.methodSignature("phone")) #[['string', 'string']]
    
    result = re_ans1.phone("Bert") #555-ITALY
    print(result)


```
得到第14关入口: http://www.pythonchallenge.com/pc/return/italy.html
## 3.知识点
1.xmlrpc: 是一种使用HTTP协议传输XML格式文件来获取远程程序调用（Remote Procedure Call）的传输方式   
2.curl命令的用法。





