'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
def check( value, against ):
	if( value % against > 0 ):
		return False
	elif( against > 1 ):
		return check( value, against - 1 )
	else:
		return True

value = 2520
answer = 0
keepGoing = True
while( keepGoing ):
	if( check( value, 20 ) ):
		answer = value
		keepGoing = False
	value += 1

print answer
