class Circle:
    pi=3.14 #class variable
    def __init__(self , radius):
        self.radius=radius
    def circumference(self):
        return 2*Circle.pi*self.radius
    def area(self):
        return Circle.pi*self.radius**2
c1=Circle(23)
print(c1.circumference())
print(c1.area())

