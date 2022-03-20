import pickle
from requests import get

p = pickle.loads(get("http://www.pythonchallenge.com/pc/def/banner.p").content)
table = [[None] * 95 for i in range(23)]
for i in range(23):
   a = 0
   for j, k in p[i]:
      for x in range(a, a + k):
         table[i][x] = j
      a += k
print("\n".join("".join(x) for x in table))
