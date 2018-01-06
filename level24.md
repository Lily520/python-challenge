# 第24关

[description](http://www.pythonchallenge.com/pc/hex/ambiguity.html)

## 1.可获知的提示有

这是一个解迷宫的问题。这里我用BFS(广度优先算法)求最短路径。


## 2.code
```python
## 24:BFS解迷宫问题
## 黑色像素(0,0,0,255)是路径，白色像素(255,255,255,255)是墙

from PIL import Image

if __name__ == "__main__":
    maze = Image.open("maze.png")
    width, height = maze.size   ##641 641
    white = (255,255,255,255)

    ##找入口,入口在第一行,像素值为(0,0,0,255), 得到入口entrance=(639, 0)
    for i in range(width):
        pixel = maze.getpixel((i,0))
        if pixel == (0,0,0,255):
            entrance = (i,0)
            break

    ## 找出口，出口在最后一行,得到出口 exit=(1, 640)
    for i in range(width):
        pixel = maze.getpixel((i,height-1))
        if pixel == (0,0,0,255):
            exit = (i,height-1)
            break

    ## BFS解迷宫
    next_map = {} #存放下一跳路径信息
    queue = [exit] #待访问节点
    direction = [[-1,0],[0,-1],[1,0],[0,1]] #方向
    while queue:
        pos = queue.pop(0)  #当前访问节点

        if pos == entrance:
            break

        for dir in direction: #遍历邻居节点
            tmp = (pos[0]+dir[0],pos[1]+dir[1])
            if tmp not in next_map.keys() and tmp[0] >= 0 and tmp[0] < width and  tmp[1] >= 0 and tmp[1] < height and maze.getpixel(tmp) != white:
                # print(maze.getpixel(tmp))
                next_map[tmp] = pos
                queue.append(tmp)

    # 按最优路径找闯关密码 RGB通道中，G和B通道的像素值都为0，R通道的像素值0和非0值交替出现，收集R通道中的非零值
    path = []
    while pos != exit:
        path.append(maze.getpixel(pos)[0])
        pos = next_map[pos]
    open('maze.zip', 'wb').write(bytes(path[1::2]))  #解压得到图片，有字母lake


    #输出最优路径
    pos = entrance
    while pos != exit:
        maze.putpixel(pos, (0, 255, 0, 255))
        pos = next_map[pos]
    maze.save("path.png")

    ###闯关密码：lake




```
得到第25关入口: http://www.pythonchallenge.com/pc/hex/lake.html










