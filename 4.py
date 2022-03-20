import re
from requests import get

ra = get("http://www.pythonchallenge.com/pc/def/equality.html").text.replace("\n", "")
t = re.findall("<!--(.*?)-->", ra)[0]
print("".join([x[4] for x in re.findall("[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]", t)]))
