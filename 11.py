def gen():
    s = "1"
    while True:
        yield s
        ns = ""
        x, y = s[0], 0
        for i in s + " ":
            if i != x:
                ns += str(y) + x
                x, y = i, 1
            else:
                y += 1
        s = ns


a = gen()
for i in range(31):
    print(len(next(a)))
