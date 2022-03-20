import re
from requests import get

ra = get("http://www.pythonchallenge.com/pc/def/ocr.html").text.replace("\n", "")
t = re.findall("<!--(.*?)-->", ra)[1]
print("".join(x for x in t if not x in "%&+$@{[()]}^_!*#"))
