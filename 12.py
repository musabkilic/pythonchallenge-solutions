import io
from PIL import Image
from requests import get
from requests.auth import HTTPBasicAuth

t = io.BytesIO(get("http://www.pythonchallenge.com/pc/return/cave.jpg",
               auth=HTTPBasicAuth("huge", "file")).content)
im = Image.open(t)
w, h = im.size
im_n = Image.new("RGB", (w // 2, h // 2))

for y in range(h):
    for x in range(w):
        p = im.getpixel((x, y))
        if (x + y) & 1 == 0:
            im_n.putpixel((x // 2, y // 2), p)
im_n.show()
