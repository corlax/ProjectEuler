'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
from math import sqrt
def nth_prime( n ):
	i = 2
	count = 0
	while( True ):
		sqr = sqrt(i)
		j = 2
		prime = True
		while j <= sqr:
			if i % j == 0:
				prime = False
			j += 1
		if prime:
			count += 1

		if count == n:
			return i

		i += 1

print nth_prime( 10001 )
