'''
Two positive numbers A and B are said to be connected (denoted by "A &harr; B") if one of these conditions holds:

(1) A and B have the same length and differ in exactly one digit; for example, 123 &harr; 173.

(2) Adding one digit to the left of A (or B) makes B (or A); for example, 23 &harr; 223 and 123 &harr; 23.





We call a prime P a 2's relative if there exists a chain of connected primes between 2 and P and no prime in the chain exceeds P.





For example, 127 is a 2's relative. One of the possible chains is shown below:

2 &harr; 3 &harr; 13 &harr; 113 &harr; 103 &harr; 107 &harr; 127

However, 11 and 103 are not 2's relatives.





Let F(N) be the sum of the primes &le; N which are not 2's relatives.

We can verify that F(103) = 431 and F(104) = 78728.





Find F(107).
'''