
while True:
	print('\nPress 1 for Addition')
	print('Press 2 for Subtraction')
	print('Press 3 for Division')
	print('Press 4 for Multiplication')
	print('Press 5 for Exit')
	choice = input('   \n   ')
	print(f'\nYour choice is:{choice}\n')


	def enteredNum():
		if choice == '5':
			exit()		
		elif choice < '1' or choice > '5':
			print('INVALID CHOICE...\n')
			return
		num1 = float(input('Enter the 1st number:'))
		num2 = float(input('Enter the 2nd number:'))
		if choice == '1':
			result = num1 + num2
			print(f'The sum of {num1} and {num2} is {result}\n')
		elif choice == '2':
				result = num1 - num2
				print(f'The Difference of {num1} and {num2} is {result}\n')
		elif choice == '3':
			result = num1 * num2
			print(f'The Multiplication of {num1} and {num2} is {result}\n')
		elif choice == '4':
			result = num1 / num2
			print(f'The Division of {num1} and {num2} is {result}\n')
	
	enteredNum()
		
	
	