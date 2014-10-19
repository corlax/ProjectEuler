'''
An integer is called B-smooth if none of its prime factors is greater than B.



Let SB(n) be the largest B-smooth divisor of n.

Examples:

S1(10) = 1

S4(2100) = 12

S17(2496144) = 5712



Define F(n) = &sum;1&le;B&le;n &sum;0&le;r&le;n SB(C(n,r)). Here, C(n,r) denotes the binomial coefficient.

Examples:

F(11) = 3132

F(1&nbsp;111) mod 1&nbsp;000&nbsp;000&nbsp;993 = 706036312

F(111&nbsp;111) mod 1&nbsp;000&nbsp;000&nbsp;993 = 22156169



Find F(11&nbsp;111&nbsp;111) mod 1&nbsp;000&nbsp;000&nbsp;993.
'''