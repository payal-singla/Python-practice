#used to access key
#if key  is not found it return none
#if we need to return something else it can return that also

d={'name': 'payal', 'age': 19, 'hobbies': 'painting', 'state': 'punjab'}
print(d.get('names'))
print(d.get('names','not found'))

#if there are two same keys ,the right overrides the left one
