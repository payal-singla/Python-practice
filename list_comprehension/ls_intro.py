#list comprehension is used to short the code
#its bsic use is to define python as less lines of code
#for example
squares=[]
for i in range(1,11):
    squares.append(i*i)
print(squares)
#with list comprehension
square=[i*i for i in range(1,11)]
print(square)
#above both gives the same output and you can see the difference between length of code
