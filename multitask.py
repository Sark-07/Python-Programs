from time import sleep
from threading import Thread

ch = input("Press y or Y to continue:\n")
if ch == "y" or "y":
    class multi(Thread):
        def run(self):
            a = ["Tui", "Ki", "Janis", "Tui", "Ekta", "Asto", "Bokachoda"]
            for i in a:
                print(i, end="  ")
                sleep(1)


    m = multi()
    m.start()
    m.join()
    print("\n\n")
    print("Etai bolar chilo!!")
    sleep(2)
else:
    exit(0)
