#when function return two values its a tuple
def func(num1,num2):
    add=num1+num2
    multi=num1*num2
    return add,multi
print(func(4,6))
print(type(func(4,6)))

