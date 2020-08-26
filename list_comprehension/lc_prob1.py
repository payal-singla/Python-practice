#return a list with opposite string
lists=['abc','asd','wedxs','dfc','efcs']
print(lists)
#with regular


list1=[]
for i in lists:
    list1.append(i[::-1])
print(list1)
#2nd method
list2=[i[::-1] for i in lists] 
print(list2)