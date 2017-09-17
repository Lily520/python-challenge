#11  图像奇偶像素的拆分

from PIL import Image

if __name__ == "__main__":

    img = Image.open("cave.jpg")
    width, height = img.size

    odd = Image.new(img.mode,(width//2,height//2)) #奇数
    even = Image.new(img.mode,(width//2,height//2)) #偶数

    for w in range(width):
        for h in range(height):
            get_color = img.getpixel((w,h))

            if (w+h) % 2 == 0:
                even.putpixel((w//2,h//2),get_color)
            else:
                odd.putpixel((w//2,h//2),get_color)

    # even.show() #evil
    odd.show()