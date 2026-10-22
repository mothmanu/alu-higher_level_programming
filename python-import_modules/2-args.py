#!/usr/bin/python3
if len(argv) == 0:
    print("0 arguments.")
else:
    count = 1
    for str in argv:
        if str == " ":
            index = str.find(" ")
            word = argv[:index+1]
            print("{:d}: {}".format(count, word))
            count += 1
            argv.replace(word,"")
            
