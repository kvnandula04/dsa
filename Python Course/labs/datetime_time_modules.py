from datetime import time, datetime

dt = datetime(2020, 11, 4, 14, 53, 00)

print(dt.strftime("%Y/%m/%d %H:%M:%S"))
print(dt.strftime("%y/%B/%d %H:%M:%S PM"))
print(dt.strftime("%a, %Y %b %d"))
print(dt.strftime("%A, %Y %B %d"))
print(dt.strftime("Weekday: %w"))
print(dt.strftime("Day of the year: %j"))
print(dt.strftime("Week number of the year: %W"))

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt1 = datetime(2020, 9, 29, 14, 41, 0)
dt2 = datetime(2020, 9, 28, 14, 41, 0)

print(dt1 - dt2)
