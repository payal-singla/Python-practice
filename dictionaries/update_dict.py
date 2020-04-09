#update is used to combine two dix=ctionaries
data1 = dict(name= "payal", age=19)
data2=dict(hobbies='painting', state='punjab')
data1.update(data2)
print(data1)
print(data1.pop('punjab'))
print(data1)