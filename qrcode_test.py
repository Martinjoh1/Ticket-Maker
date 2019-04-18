import qrcode
from PIL import Image

img = qrcode.make("Hello World"+"\n"+"This is a valid ticket")
img.save("image.png")
