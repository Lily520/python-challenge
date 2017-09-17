from PIL import Image

if __name__ == "__main__":

    #step1: 计算图的相关信息
    png = Image.open("oxygen.png")
    width,height = png.size #获取图像尺寸
    print(png.format) #PNG
    print(width,height) #629, 95
    print(png.mode) #RGBA

    #step2: 求模糊区域的高度 (10,43)-(10,51)处的像素值相同 height = 9
    # pre_values = png.getpixel((10,0))
    # count = 0
    # for y in range(0,95):
    #     place = (10,y)
    #     values = png.getpixel(place) #获取place位置处的像素值
    #     print(values,"  ", place)
    #     if values == pre_values:
    #         count += 1
    #     else:
    #         print("values: ", values, " count: ",count)
    #         count = 1
    #         pre_values = values


    #step3: 求模糊区域的宽度:  0-607  1个5像素，85*7像素，1*8像素
    # pre_values = png.getpixel((0,48))
    # count = 0
    # count_7 = 0
    # for x in range(0,629):
    #     position = (x,48)
    #     values = png.getpixel(position)
    #     print(values, "  ", position)
    #     if values == pre_values:
    #         count += 1
    #     else:
    #         print("pre_values: ", pre_values, " count: ",count)
    #         count = 1
    #         pre_values = values

    # step4: 初步获取信息
    # im = png.crop((0,43,607,51)).convert("L")
    # size = im.size
    # size0 = size[0]
    #
    # values = im.getpixel((0,3)) #第一个5像素
    # res = []
    # res.append(chr(values))
    # for x in range(5,size0,7): #85个7像素
    #     values = im.getpixel((x,3))
    #     print(values,":: ",chr(values))
    #     res.append(chr(values))
    #
    # ans = "".join(res)
    # #print(res)
    # print(ans) #smart guy, you made it. the next level is [105, 10, 16, 101, 103, 14, 105, 16, 121

    # step5: 得到最终结果
    ans_list = [105,110,116,101,103,114,105,116,121]
    res2 = ""
    for ele in ans_list:
        print(ele,": ",chr(ele))
        res2 += chr(ele)
    print(res2) #integrity
