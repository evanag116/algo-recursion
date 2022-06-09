def factorial(x):
	if x < 2:
		return 1
	else:
		return x * factorial(x-1)

def palindrome(str):
	if len(str) < 2:
		return True
	if str[0] == str[-1]:
		return palindrome(str[1:-1])
	else:
		return False

def bottles(num):
	original_number = num

	def recursion(num):
		if num == 1:
			return f"""
Take one down and pass it around, 1 bottle of beer on the wall.
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, {original_number} bottles of beer on the wall.
			"""
		else:
			return f"""
{num} bottles of beer on the wall, {num} bottles of beer.
Take one down and pass it around, {num-1} bottles of beer on the wall. {recursion(num-1)}""" 

	return recursion(num)




def roman_num(num):
	pass

