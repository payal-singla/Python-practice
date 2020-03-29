def square_list(l):
    list2 = []
    for i in l:
        list2.append(i**2)
    return list2
numbers= list(range(1,11))
print(square_list(numbers))
#list is called with arguement l
