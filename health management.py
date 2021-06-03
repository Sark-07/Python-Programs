from pathlib import Path
print("Health Management software")
print("Please make sure that your exercise file and food file has a unique name!!")


def get_time():
    from datetime import datetime
    return datetime.now()


def take(n):
    if n == 1:
        t = int(input("Do you want add items after where you left or overwrite? If continue press 1 else press 2:\n"))
        if t == 2:
            l = int(input("Do you want to lock exercises or foods? if exercise press 1 else press 2:\n"))
            if l == 1:
                name = input("Enter your name:\n")
                path = Path(name+".txt")
                if path.exists():
                    print("This name already exits.Please enter with another name!!")
                else:
                    fp = open(name + ".txt", "w")
                    k = 'y'
                    while k != 'n':
                        text = input("Enter your data:\n")
                        fp.write("" + text + ":" + " (" + str(get_time()) + ")" + "\n")
                        k = input("Do you want to add more them press y else press 1:\n")
                    fp.close()
            elif l == 2:
                name = input("Enter your name:\n")
                path = Path(name + ".txt")
                if path.exists():
                    print("This name already exits.Please enter with another name!!")
                else:
                    fp = open(name + ".txt", "w")
                    k = 'y'
                    while k != 'n':
                        text = input("Enter your data:\n")
                        fp.write("" + text + ":" + " (" + str(get_time()) + ")" + "\n")
                        k = input("Do you want to add more them press y else press 1n:\n")
                    fp.close()
        elif t == 1:
            l = int(input("Do you want to add more exercises or foods? if exercise press 1 else press 2:\n"))
            if l == 1:
                name = input("Enter your name:\n")
                fp = open(name + ".txt", "a")
                k = 'y'
                while k != 'n':
                    text = input("Enter your data:\n")
                    fp.write("" + text + ":" + " (" + str(get_time()) + ")" + "\n")
                    k = input("Do you want to add more them press y else press 1n:\n")
                fp.close()
            elif l == 2:
                name = input("Enter your name:\n")
                fp = open(name + ".txt", "a")
                k = 'y'
                while k != 'n':
                    text = input("Enter your data:\n")
                    fp.write("" + text + ":" + " (" + str(get_time()) + ")" + "\n")
                    k = input("Do you want to add more them press y else press 1n:\n")
                fp.close()
    elif n == 2:
        print("What do you want retrieve exercises or foods? If exercises enter your exercise file name else enter "
              "your food file name:\n")
        file_name = input("Enter your file name please:\n")
        path = Path(file_name+".txt")
        if path.exists():
            with open(file_name + ".txt", "r") as ft:
                if ft is None:
                    print("There is no data!!\n Please enter your data first!!")
                else:
                    for line in ft:
                        print(line, end="")
        else:
            print("Invalid file name.Please enter your file name correctly!!")
    else:
        print("Invalid input!!")


n = int(input("If you want to lock items press 1 or if you want to retrieve items press 2:\n"))
take(n)
