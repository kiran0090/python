mydict1 = {'name': 'kiran', 'age': 23, 'city': 'bangalore'}
print(mydict1)

# OR

mydict2 =  dict(name= 'kiran', age= 23, city= 'bangalore')
print(mydict2)

# accessing elements
values = mydict1['name']
print(values)

# adding an element
mydict1['hobbie'] = 'coding'
print(mydict1)

# deleting elements
del mydict1['hobbie']
print(mydict1)

# OR

mydict2.pop('age')
print(mydict2)

# looping through dictionaries
for key, value in mydict1.items():
	print(key,':', value)

# copying dictionaries, will also affect the original dictionary
dict_cpy = mydict2
dict_cpy['lastname'] = 'iyer'
print(mydict2)
print(dict_cpy)

# updating dictionaries
mydict3 = {'name': 'kavya', 'age': 17, 'city': 'mangalore'}
mydict4 = dict(name= 'kumar', age= 44, city= 'mysore')
mydict3.update(mydict4)
print(mydict3)