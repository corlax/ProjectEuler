'''
For every integer n&gt;1, the family of functions fn,a,b  is defined 

by fn,a,b(x)&equiv;ax+b mod n for a,b,x integer and  0&lt;a&lt;n, 0&le;b&lt;n, 0&le;x&lt;n.

We will call fn,a,b a retraction if fn,a,b(fn,a,b(x))&equiv;fn,a,b(x) mod n for every 0&le;x&lt;n.

Let R(n) be the number of retractions for n.





You are given that

&sum; R(c) for c=C(100 000,k), and 1 &le; k &le;99 999 &equiv;628701600 (mod 1 000 000 007).

(C(n,k) is the binomial coefficient).



 

Find &sum; R(c) for c=C(10 000 000,k), and 1 &le;k&le; 9 999 999.

Give your answer modulo 1 000 000 007.
'''