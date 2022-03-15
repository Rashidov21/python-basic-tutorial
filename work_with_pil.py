# pip install Pillow
from PIL import Image, ImageFilter

im1 = Image.open("images/python.png")
# im2 = Image.open("images/rocket.png").resize((512,512), resample=True)
# im1.filter(ImageFilter.CONTOUR()).show()
# im1.show()
dark_back = Image.new("RGBA", (512,512),"blue")
# image.show()
alpha_image = Image.alpha_composite(dark_back, im1)
alpha_image.show()

# alpha_image.show()


# with Image.open("images/python.png") as im:
#     im.rotate(45).show()
# print(type(myimage))
# print(dir(myimage))
# myimage.load() # rasm uchun hamma funclar ochiladi
# small = myimage.resize((100,100), resample=True)
# print(small.size) # 100x100
# small.show()
# blurred = myimage.filter(ImageFilter.BLUR)
# myimage.show()
# blurred.show()
# # сохраняем изображение
# blurred.save("blurred.png")
# try:
#     original = Image.open("Lenna.png")
# except FileNotFoundError:
#     print("Файл не найден")

# print("Размер изображения:")
# print(myimage.format, myimage.size, myimage.mode)

# открываем оригинал и размытое изображение
