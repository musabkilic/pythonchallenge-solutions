import datetime
for x in range(1006, 2006, 10):
    s = datetime.datetime(year=x, month=1, day=26).weekday()
    if s == 0:
        print(x)
