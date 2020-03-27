def odd_even(num):
    if num%2 == 0:
        return("even")
    return('odd')
    
num=int(input("enter number:" ))
print(odd_even(num))
