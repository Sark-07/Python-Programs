class addition:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        a1 = self.m1 + other.m1
        a2 = self.m2 + other.m2
        t = addition(a1, a2)
        return t


t1 = addition(int(input("Enter first num:\n")), int(input("Enter first num:\n")))
t2 = addition(int(input("Enter first num:\n")), int(input("Enter first num:\n")))
t = t1 + t2
print(t.m1, t.m2)
