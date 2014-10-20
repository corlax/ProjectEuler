'''
A Pythagorean triplet is a set of three natural numbers, a &lt; b &lt; c, for which,

 a2 + b2 = c2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
def pyth():
	for a in range( 1,1001 ):
		for b in range( 1, 1001):
			for c in range( 1, 1001 ):
				if ( ( ( ( a**2 ) + ( b**2 ) ) == (c**2) ) and (a + b + c) == 1000 ):
					return a * b * c
				
print pyth()
