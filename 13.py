import io
from PIL import Image, ImageFile
from requests import get
from requests.auth import HTTPBasicAuth
ImageFile.LOAD_TRUNCATED_IMAGES = True


gfx = io.BytesIO(get("http://www.pythonchallenge.com/pc/return/evil2.gfx",
                     auth=HTTPBasicAuth("huge", "file")).content)
files = [b""] * 5
t = gfx.tell() - 1
while t != gfx.tell():
    t = gfx.tell()
    for i in range(5):
        files[i] += gfx.read(1)

im = Image.new("RGB", (640 * 5, 480))
for i in range(5):
    im_n = Image.open(io.BytesIO(files[i])).resize((640, 480))
    im.paste(im_n, (640 * i, 0))
im.show()
