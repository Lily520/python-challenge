# 第15关

[description](http://www.pythonchallenge.com/pc/return/uzi.html)

## 1.可获知的提示有  
**`hint1`**:年份：1XX6年

**`hint2`**:2月有29天：闰年(能被4整除而不能被100整除，或者能被400整除)

**`hint3`**:1月26是周一

**`hint4`**:源代码中的两句话：    
     he ain't the youngest, he is the second   
     todo: buy flowers for tomorrow 

因此，我们要求的就是离现在次近的年份，并且在1.27出生的人

## 2.code
```python
from datetime import datetime
import calendar


if __name__ == "__main__":

    leap_year = []
    for year in range(1006, 1997, 10):
        # if((year % 4 == 0 and year % 100 != 0)or(year % 400 == 0)) and (datetime.isoweekday(datetime(year,1,26))==1):#闰年,1.26周一
        if calendar.isleap(year) and datetime.isoweekday(datetime(year, 1, 26)) == 1:  # 闰年 1.26周一
            leap_year.append(year)

    print(leap_year[-2])  # 目标年份 1756  1756.1.27是mozart的生日

```
得到第16关入口: http://www.pythonchallenge.com/pc/return/mozart.html  
## 3.知识点
1.datetime.isoweekday(): 求星期几  
2.calendar.isleap(year)：是不是闰年，是返回True






