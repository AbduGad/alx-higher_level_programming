#!/usr/bin/python3
first = 0
second = 0
while first < 7:
    if second == 9:
        first += 1
        second = first + 1
    else:
        second += 1
    print("{}{}".format(first, second), end=", ")
print("79, 89")
