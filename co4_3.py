class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def lt(r1, r2):
       return r1.area() < r2.area()

r1 = Rectangle(10, 5)
r2 = Rectangle(8, 8)

if r1.area()>r2.area():
    print("Rectangle 1 has smaller area")
else:
    print("Rectangle 2 have smaller area")