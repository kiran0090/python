mylists = ['kiran', 'kumar', 'srikanth']
a = 0
for x in mylists:
	a+=1
	print(mylists,a)

print(len(mylists))

mylists.append('sridar')
print(mylists)

mylists.insert(2, 'gagan')
print(mylists)

item = mylists.pop()
print(item)
print(mylists)


# reversing a list
mylist = [1, 2, 3, 4, 5, 6, 7]
a = mylist[::-1]
print(a)


# list copying
org_list = ['apple', 'banana', 'orange']
cpy_list = org_list
cpy_list.append('lemon')
print(cpy_list)
print(org_list)

list1 = [1, 2, 3, 4, 5, 6, 7]
a = [q*q for q in list1]
print(list1)
print(a)