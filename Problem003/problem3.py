'''
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

'''
The is_prime function courtesy of: http://en.wikipedia.org/wiki/Primality_test#Python_implementation
'''
def is_prime(n):
	if n <= 3:
		return n >= 2
	if n % 2 == 0 or n % 3 == 0:
		return False
	for i in range(5, int(n ** 0.5) + 1, 6):
		if n % i == 0 or n % (i + 2) == 0:
			return False
	return True
'''
The factors function courtesy of: http://stackoverflow.com/a/6800214/833696
'''
def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

largest = 0;
for x in factors( 600851475143 ):
	if( is_prime( x ) and x > largest):
		largest = x

print largest
