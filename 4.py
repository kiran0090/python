# # p = (2, 3, 'r')
# # print(p * 2)

# def add(a, b):
# 	return a+4, b+3
# result = add(3, 4)
# print(result)

print('Welcome to MY_BANK ATM')
restart = ('y')
chances = 3
balance = 10000.00
while chances >= 0:
	pin = int(input('Please Enter your 4 digit PIN: '))
	if pin == (1234):
		while restart not in ('n', 'NO', 'no', 'N'):
			print('You entered you pin correctly')
			print('Please Press 1 for your Balance')
			print('Please Press 2 to Make a Withdrawl')
			print('Please Press 3 to Pay in')
			print('Please Press 4 to return Card \n')
			option = int(input('What would you like to choose? '))
			if option == 1:
				print('Your Balance is $', balance)
				restart = input('Would you like to go back? ')
				if restart in ('n', 'NO', 'no', 'N'):
					print('Thank you')
					break
			elif option == 2:
				option = ('y')
				Withdrawl = float(input('How much would you like to Withdraw? 20, 40, 60, 80, 100 for other entet=r 1: '))
				if  Withdrawl in [ 20, 40, 60, 80, 100]:
					balance = balance - Withdrawl
					print('\n Your balance is now $', balance)
					restart = input('Would you like to go back? ')
					if restart in('n', 'NO', 'no', 'N'):
						print('Thank you')
						break
					elif Withdrawl != [10, 30, 50, 70, 90]:
						print('Invalid Amount, please Re-type \n')
						restart = ('y')
			elif option == 3:
				pay_in = float(input('How much would you like to pay-in? '))
				balance = balance + pay_in
				print('\n Your balance is now $', balance)
				restart = input('Would you like to go back? ')
				if restart in ('n', 'NO', 'no', 'N'):
					print('Thank You')
					break
			elif option == 4:
				print('Please wait..')
				print('Thank You for your service')
				break
	else:
		print('Please enter a vaild number. \n')
		# restart('y')
	if pin != (1234):
		print('Incorrect Password')
		chances = chances - 1
	if chances == 0:
		print(' \n No more tries')
		break