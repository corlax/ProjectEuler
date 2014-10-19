'''
Let {a1, a2,..., an} be an integer sequence of length n such that:



a1 = 6

for all 1 &le; i < n : &phi;(ai) < &phi;(ai+1) < ai < ai+1 1



Let S(N) be the number of such sequences with an &le; N.

For example, S(10) = 4: {6}, {6, 8}, {6, 8, 9} and {6, 10}.

We can verify that S(100) = 482073668 and S(10 000) mod 108 = 73808307.



Find S(20 000 000) mod 108.



1 &phi; denotes Euler's totient function.
'''