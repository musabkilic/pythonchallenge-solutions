from requests import get

L = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
n = "12345"
while n:
    t = get(L + n).text
    g = t[24:]
    n = g
    print(t)
