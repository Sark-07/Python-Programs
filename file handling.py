fp = open("file.txt", "w")
fp.write("This is my\n"
         "first\n"
         "file")
f = open("file handling.py", "r")
for i in f:
    print(i)
