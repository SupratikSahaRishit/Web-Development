class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.1416 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.1416 * self.radius

c1 = Circle(7)

print("Radius:", c1.radius)
print("Area of Circle:", c1.area())
print("Perimeter of Circle:", c1.perimeter())