while True:
	print('Press 1 for Addition')
	print('Press 2 for Subtraction')
	print('Press 3 for Multiplication')
	print('Press 4 for Division')
	print('Press 5 for Exit\n')
	choice = input('   ')
	print(f'\nYour choice is:{choice}\n')

	def add():
		num1 = float(input('Enter the 1st number:'))
		num2 = float(input('Enter the 2nd number:'))
		result = num1 + num2
		print(f'The Sum of {num1} and {num2} : {result}\n')
		return add
	def multi():
		num1 = float(input('Enter the 1st number:'))
		num2 = float(input('Enter the 2nd number:'))
		result = num1 * num2
		print(f'The Sum of {num1} and {num2} : {result}\n')
		return multi
	def sub():
		num1 = float(input('Enter the first number:'))
		num2 = float(input('Enter the second number:'))
		result = num1 - num2
		if num1 > num2:
			result = num1 - num2
		else:
			result = num2 - num1
			print(f'The Difference of {num1} and {num2} : {result}\n')
		return sub
	def div():
		num1 = float(input('Enter the 1st number:'))
		num2 = float(input('Enter the 2nd number:'))
		result = num1 / num2
		print(f'The Sum of {num1} and {num2} : {result}\n')
		return div	


	if choice == '1':
		add()
		

	elif choice == '2':
		sub()
		
	elif choice == '3':
		multi()

	elif choice == '4':
		div()

	elif choice == '5':
		exit()

	elif choice < '1' or choice > '5':
		print('Enter a valid choice...\n')






