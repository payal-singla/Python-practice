#Problem statement
#make a function which takes input as integer (n)
#returns a dictionary cointaing cube of numbers from 1 to n 

#example
#cube_finder(3)
#{1:1,2:8,3:27}

def cube_finder(n):
    cubes= dict()
    for i in range(1,n):
        cubes[i]=i*i*i
    return cubes
print(cube_finder(int(input())))


