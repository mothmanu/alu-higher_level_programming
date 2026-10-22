#!/usr/bin/python3
if __name__ == "__main__":
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
            
