class student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show(self):
        print(self.name, self.roll)


s1 = student(input("Enter the name:\n"), input("Enter the roll number:\n"))
s1.show()
