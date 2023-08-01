import random
start = input('Please enter the minimum number in this game: ')
start = int(start)
end = input('Please enter the maximum number in this game: ')
end = int(end)

code = random.randint(start, end)
count = 0
while True:
	number = input('Please enter your number: ')
	number = int(number)
	count = count + 1 #可寫成count += 1
	if number == code:
		print('You crack the code! ')
		print('It takes you', count, 'times')
		break
	elif number > code:
		print('The code is smaller.')
	elif number < code:
		print('The code is bigger. ')