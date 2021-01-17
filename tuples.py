mytuple = tuple(['kiran', 23, 'bangalore'])
print(mytuple)

for c in mytuple:
	print(c)

if 'kiran' in mytuple:
	print('yes')
else:
	print('no')

my_tuple = ['b', 'a', 'n', 'g', 'a', 'l', 'o', 'r', 'e']	
print(my_tuple.count('x'))
print(my_tuple.index('e'))


# tuple to list
my_list = list(my_tuple)
print(my_list)

# list to tuple
my_tuple2 = tuple(my_list)
print(my_tuple2)

a = (1, 2, 3, 4, 5, 6, 7, 8)
b = a[2:5]  #slice
print(b)

c = a[::3] #step argument
print(c)

my_tuple3 = 'kiran', 23, 'bangalore' #unpacking tuple
name, age, city = my_tuple3  
print(name)
print(age)
print(city)

#space allocated for tuple VS lists
import sys
my_list4 = [0, 1, 2, 3, 'hello', True]
my_tuple4 = (0, 1, 2,3, 'hello', True)
print(sys.getsizeof(my_list4), 'bytes')
print(sys.getsizeof(my_tuple4), 'bytes')

#time taken to compile for tuple VS lists
import timeit
print(timeit.timeit(stmt='[1, 2, 3, 4, 5, 6]', number=10000000))
print(timeit.timeit(stmt='(1, 2, 3, 4, 5, 6)', number=10000000))