from PIL import Image
import numpy as np

if __name__ == "__main__":


    img = Image.open("mozart.gif")
    width, height = img.size

    # 根据图mozart知，若粉色在每行都出现，则（出现次数）% height==0
    hist = img.histogram()
    pink = [(num, hist.index(num)) for num in hist if (num % height == 0 and num != 0)]  # (出现次数,像素)

    data = img.getdata()
    data = np.array(data).reshape((height, width))
    print(data.shape)
    shiftData = np.array(
        [np.roll(data[row, :], -data[row, :].tolist().index(pink[0][1])) for row in range(height)])  # 将pink颜色移到前面
    shiftData.shape = (height * width,)  # 根据提示: let me get this straight
    print(shiftData.shape)
    img.putdata(shiftData)
    img.show() #romance