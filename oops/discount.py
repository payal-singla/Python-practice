class Laptop:
    def __init__(self,brand,model,price):
        self.b=brand
        self.m=model
        self.p=price
    
    def discount(self,amount):
        return self.p-((amount/100)*self.p)

p1=Laptop('HP','IDK',50000)
p2=Laptop('DELL','IDK',40000)
print(p1.discount(40))


