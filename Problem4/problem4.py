'''
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers
'''
def palindrom():
	largest = 0
	one = 999
	while one > 99:
		two = 999
		while two > 99:
			value = one * two
			if( str(value) == str(value)[::-1] ):
				if( value > largest ):
					largest = value

			two -= 1
		one -= 1
	return largest

print palindrom()
