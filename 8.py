import io
from PIL import Image
from requests import get

t = io.BytesIO(get("http://www.pythonchallenge.com/pc/def/oxygen.png").content)
im = Image.open(t)

msg = ""
for x in range(4, 608, 7):
    msg += chr(im.getpixel((x, 45))[0])
print(msg)
print("".join(chr(x) for x in eval(msg[42:])))
