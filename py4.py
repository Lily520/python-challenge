#4 网络爬虫

import urllib.request

if __name__ == "__main__":
    src = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345") #初始url "="后面依次为12345,8022

    nexturl = None
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

    count = 0
    while True:
        lines = str(src.read())
        print(lines)
        splits = lines.strip("\'").strip("\n").split(" ")
        print(splits[-1]) #splits[-1]是获取到的下一个nothing=后面的数字
        try:
            nextid = int(splits[-1])
        except:
            break
        nexturl = url + str(nextid) #下一个url
        count += 1
        print(count, "::: ", nexturl)
        src.close()
        src = urllib.request.urlopen(nexturl)
