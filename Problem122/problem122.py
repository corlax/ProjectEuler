'''
The most naive way of computing n15 requires fourteen multiplications:

n &times; n &times; ... &times; n = n15

But using a &quot;binary&quot; method you can compute it in six multiplications:

n &times; n = n2

n2 &times; n2 = n4

n4 &times; n4 = n8

n8 &times; n4 = n12

n12 &times; n2 = n14

n14 &times; n = n15

However it is yet possible to compute it in only five multiplications:

n &times; n = n2

n2 &times; n = n3

n3 &times; n3 = n6

n6 &times; n6 = n12

n12 &times; n3 = n15

We shall define m(k) to be the minimum number of multiplications to compute nk; for example m(15) = 5.

For 1 &le; k &le; 200, find &sum; m(k).
'''