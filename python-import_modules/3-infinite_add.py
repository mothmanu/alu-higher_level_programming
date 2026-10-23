#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total = 0
    for item in argv[1:]:
        total += int(item)
    print("{:d}".format(total))
