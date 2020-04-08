#items() is used to display and diffenrentiate bt=etween all the items in the dictionaries
data1 = dict(name= "payal", age=19)

print(data1.items())
# it gives tuples in the list

for key,value in data1.items():
    print(f"key is {key} and value is {value}")
