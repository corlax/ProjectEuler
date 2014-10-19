'''
For any positive integer k, a finite sequence ai of fractions xi/yi is defined by:

a1 = 1/k and

ai = (xi-1+1)/(yi-1-1) reduced to lowest terms for i>1.

When ai reaches some integer n, the sequence stops. (That is, when yi=1.)

Define f(k) = n. 

For example, for k = 20:







1/20 &rarr; 2/19 &rarr; 3/18 = 1/6 &rarr; 2/5 &rarr; 3/4 &rarr; 4/3 &rarr; 5/2 &rarr; 6/1 = 6







So f(20) = 6.







Also f(1) = 1, f(2) = 2, f(3) = 1 and &Sigma;f(k3) = 118937 for 1 &le; k &le; 100.







Find &Sigma;f(k3) for 1 &le; k &le; 2&times;106.
'''