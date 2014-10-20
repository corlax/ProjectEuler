'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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

total = 0
for i in range( 1, 2000000 ):
	if( is_prime( i ) ):
		total += i

print total
