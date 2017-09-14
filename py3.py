#3.正则表达式

import re

if __name__ == "__main__":
    str = "" #太长省略，运行前要先替换成原网页中的字符串
    s = re.findall('[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}',str) #一个小写字母两边恰被3个大写字母包围
    result = [x[4] for x in s]
    print(result) #linkedlist