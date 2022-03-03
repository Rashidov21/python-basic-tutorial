# pip install -U pyxel
from path import Path
from main import gen_qr_code


text = "текст для шифровки в QR код"
path_to_download = Path().joinpath("example", "example.jpg")
path_to_save = Path().joinpath("example", "example.png")

gen_qr_code(text, path_to_download, path_to_save)