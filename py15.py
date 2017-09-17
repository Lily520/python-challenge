from datetime import datetime
import calendar


if __name__ == "__main__":

    leap_year = []
    for year in range(1006, 1997, 10):
        # if((year % 4 == 0 and year % 100 != 0)or(year % 400 == 0)) and (datetime.isoweekday(datetime(year,1,26))==1):#闰年,1.26周一
        if calendar.isleap(year) and datetime.isoweekday(datetime(year, 1, 26)) == 1:  # 闰年 1.26周一
            leap_year.append(year)

    print(leap_year[-2])  # 目标年份 1756  1756.1.27是mozart的生日