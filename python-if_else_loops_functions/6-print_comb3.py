#!/usr/bin/python3
for i in range(10):
    print("{:02d, }".format(i), end = "")
for i in range(12,89):
    if i % 11 != 0 or i % 10 != 0:
        print("{:2d, }".format(i), end = "") 
print("{:d}".format(89)
