from PIL import Image, ImageDraw

if __name__ == "__main__":
    first = [] #太长省略，运行之前记得补全
    second = [] #太长省略，运行之前记得补全

    image = Image.open("good.jpg")
    draw = ImageDraw.Draw(image)

    # fill=(R,G,B) R,G,B的值都在0-255之间
    draw.line(first, fill=(255, 0, 0))
    draw.line(second, fill=128)
    image.show()