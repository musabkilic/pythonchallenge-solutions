import re
import turtle
from requests import get
from requests.auth import HTTPBasicAuth

ra = get("http://www.pythonchallenge.com/pc/return/good.html",
         auth=HTTPBasicAuth("huge", "file")).text.replace("\n", "")
t = re.findall("<!--(.*?)-->", ra)[1]
first = list(map(int, t[20:1772].split(",")))
second = list(map(int, t[1779:].split(",")))

t = turtle.Turtle()
turtle.setworldcoordinates(0, -500, 600, 100)
t.penup()
t.goto(first[0], -first[1])
t.pendown()
t.color("blue")
t.begin_fill()
for i in range(0, len(first), 2):
    t.goto((first[i], -first[i+1]))
t.end_fill()
t.penup()
t.goto(second[0], -second[1])
t.pendown()
t.color("red")
t.begin_fill()
for i in range(0, len(second), 2):
    t.goto((second[i], -second[i+1]))
t.end_fill()
input()
