from PIL import Image, ImageFilter

def shortImg(img, height, width):
    size = (height, width)
    saved = "test.png"
    img.thumbnail(size)
    img.save(saved)
    img.show()
try:
    img = Image.open("images/python.png")
    print(img.format , img.size, img.mode)
    blurred = img.filter(ImageFilter.BLUR)
    shortImg(img, 300,300)
    # img.show() # standart dastur ishga tushiradi
    # blurred.show()
except FileNotFoundError:
    print("Файл не найден")