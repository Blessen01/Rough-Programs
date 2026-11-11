class Time:
    def __init__(self, h, m, s):
        self.__hour = h
        self.__minute = m
        self.__second = s

    def __add__(self, other):
        s = self.__second + other.__second
        m = self.__minute + other.__minute
        h = self.__hour + other.__hour

        if s >= 60:
            m += 1
            s -= 60

        if m >= 60:
            h += 1
            m -= 60

        return Time(h, m, s)

    def display(self):
        print(self.__hour, ":", self.__minute, ":", self.__second)


t1 = Time(2, 30, 40)
t2 = Time(1, 20, 30)

t3 = t1 + t2

print("First Time:")
t1.display()

print("Second Time:")
t2.display()

print("Sum of Time:")
t3.display()