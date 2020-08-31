class Person:
    def __init__(self,f,l,age):
        self.first=f
        self.last=l
        self.age=age
    def full(self):
        return f"{self.first} {self.last}"
    def above_18(self):
        return self.age>18
p1=Person("payal",'singla',19)
p2=Person("keshav",'singla',15)
print(p1.first)
print(p1.full())
print(p1.above_18())
print(p2.above_18())

