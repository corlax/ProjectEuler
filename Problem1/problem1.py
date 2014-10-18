'''
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
answer = []
for x in range(1, 1000):
	modulo = x % 3
	if modulo == 0:
		answer.append( x )
		continue
	modulo = x % 5
	if modulo == 0:
		answer.append( x )
		continue

total = 0
for x in answer:
	total += x

print total
