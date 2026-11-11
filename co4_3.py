cclass Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __lt__(self,other):
       return self.area() < other.area()

r1 = Rectangle(9, 5)
r2 = Rectangle(2, 8)

if r1>r2:
    print("Rectangle 1 has smaller area")
else:
    print("Rectangle 2 have smaller area")

