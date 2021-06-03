class factorial:
    def __init__(self):
        self.res = self.cal(int(input("Enter the number:\n")))

    def show(self):
        print("The factorial is:")
        self.res.show()

    class cal:
        def __init__(self, fact):
            self.f = 1
            for i in range(1, fact + 1):
                self.f *= i

        def show(self):
            print(self.f)


f1 = factorial()
f1.show()
