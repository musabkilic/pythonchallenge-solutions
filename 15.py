import io
from PIL import Image
from requests import get
from requests.auth import HTTPBasicAuth

t = io.BytesIO(get("http://www.pythonchallenge.com/pc/return/wire.png",
                   auth=HTTPBasicAuth("huge", "file")).content)
im = Image.open(t)
im_n = Image.new("RGB", (100, 100))
DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]
d = 0
n = 0
p = [0, 0]
while n < 10000:
    im_n.putpixel(p, im.getpixel((n, 0)))
    np = (p[0] + DIR[d][0], p[1] + DIR[d][1])
    if not (0 <= np[0] < 100) or not (0 <= np[1] < 100) or im_n.getpixel(np) != (0, 0, 0):
        d = (d + 1) % 4
    p = [p[0] + DIR[d][0], p[1] + DIR[d][1]]
    n += 1
im_n.show()
