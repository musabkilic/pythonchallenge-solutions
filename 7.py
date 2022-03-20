import io
import zipfile
from requests import get

t = io.BytesIO(get("http://www.pythonchallenge.com/pc/def/channel.zip").content)
z = zipfile.ZipFile(t)
print(z.open("readme.txt").read().decode("ascii"))
n = "90052"
S = ""
while n.isdigit():
   t = z.open(n+".txt").read().decode("ascii")
   S += z.getinfo(n+".txt").comment.decode("ascii")
   n = t[16:]
   print(t)

print(S)
