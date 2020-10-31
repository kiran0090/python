while True:
	print('Press 1 for Addition')
	print('Press 2 for Subtraction')
	print('Press 3 for Multiplication')
	print('Press 4 for Division')
	print('Press 5 for Exit\n')
	choice = input('   ')
	print(f'\nYour choice is:{choice}\n')

	if choice == '1':
		num1 = input('Enter the first number:')
		num2 = input('Enter the second number:')
		result = num1 + num2
		print(f'The Sum of {num1} and {num2} : {result}\n')

	elif choice == '2':
		num1 = int(input('Enter the first number:'))
		num2 = int(input('Enter the second number:'))
		result = num1 - num2
		if num1 > num2:
			result = num1 - num2
		else:
			result = num2 - num1
			print(f'The Difference of {num1} and {num2} : {result}\n')

	elif choice == '3':
		num1 = int(input('Enter the first number:'))
		num2 = int(input('Enter the second number:'))
		result = num1 * num2	
		print(f'The Multiplication of {num1} and {num2} : {result}\n')

	elif choice == '4':
		num1 = int(input('Enter the first number:'))
		num2 = int(input('Enter the second number:'))
		result = num1 / num2
		if num1 == '0':
			print('Enter valid number\n')
		else:
			print(f'The Division of {num1} and {num2} : {result}\n')

	elif choice == '5':
		exit()

	elif choice < '1' or choice > '5':
		print('Enter a valid choice...\n')






