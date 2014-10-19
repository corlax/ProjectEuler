'''
Let us consider mixtures of three substances: A, B and C. A mixture can be described by a ratio of the amounts of A, B, and C in it, i.e., (a&nbsp;:&nbsp;b&nbsp;:&nbsp;c). For example, a mixture described by the ratio (2&nbsp;:&nbsp;3&nbsp;:&nbsp;5) contains 20% A, 30% B and 50% C.



For the purposes of this problem, we cannot separate the individual components from a mixture. However, we can combine different amounts of different mixtures to form mixtures with new ratios.



For example, say we have three mixtures with ratios (3&nbsp;:&nbsp;0&nbsp;:&nbsp;2), (3&nbsp;:&nbsp;6&nbsp;:&nbsp;11) and (3&nbsp;:&nbsp;3&nbsp;:&nbsp;4). By mixing 10 units of the first, 20 units of the second and 30 units of the third, we get a new mixture with ratio (6&nbsp;:&nbsp;5&nbsp;:&nbsp;9), since:

(10&middot;3/5&nbsp;+&nbsp;20&middot;3/20&nbsp;+&nbsp;30&middot;3/10&nbsp;:&nbsp;10&middot;0/5&nbsp;+&nbsp;20&middot;6/20&nbsp;+&nbsp;30&middot;3/10&nbsp;:&nbsp;10&middot;2/5&nbsp;+&nbsp;20&middot;11/20&nbsp;+&nbsp;30&middot;4/10)

= (18&nbsp;:&nbsp;15&nbsp;:&nbsp;27) = (6&nbsp;:&nbsp;5&nbsp;:&nbsp;9)



However, with the same three mixtures, it is impossible to form the ratio (3&nbsp;:&nbsp;2&nbsp;:&nbsp;1), since the amount of B is always less than the amount of C.



Let n be a positive integer. Suppose that for every triple of integers (a, b, c) with 0 &le; a, b, c &le; n and gcd(a, b, c) = 1, we have a mixture with ratio (a&nbsp;:&nbsp;b&nbsp;:&nbsp;c). Let M(n) be the set of all such mixtures.



For example, M(2) contains the 19 mixtures with the following ratios:

{(0&nbsp;:&nbsp;0&nbsp;:&nbsp;1), (0&nbsp;:&nbsp;1&nbsp;:&nbsp;0), (0&nbsp;:&nbsp;1&nbsp;:&nbsp;1), (0&nbsp;:&nbsp;1&nbsp;:&nbsp;2), (0&nbsp;:&nbsp;2&nbsp;:&nbsp;1), 

(1&nbsp;:&nbsp;0&nbsp;:&nbsp;0), (1&nbsp;:&nbsp;0&nbsp;:&nbsp;1), (1&nbsp;:&nbsp;0&nbsp;:&nbsp;2), (1&nbsp;:&nbsp;1&nbsp;:&nbsp;0), (1&nbsp;:&nbsp;1&nbsp;:&nbsp;1), 

(1&nbsp;:&nbsp;1&nbsp;:&nbsp;2), (1&nbsp;:&nbsp;2&nbsp;:&nbsp;0), (1&nbsp;:&nbsp;2&nbsp;:&nbsp;1), (1&nbsp;:&nbsp;2&nbsp;:&nbsp;2), (2&nbsp;:&nbsp;0&nbsp;:&nbsp;1), 

(2&nbsp;:&nbsp;1&nbsp;:&nbsp;0), (2&nbsp;:&nbsp;1&nbsp;:&nbsp;1), (2&nbsp;:&nbsp;1&nbsp;:&nbsp;2), (2&nbsp;:&nbsp;2&nbsp;:&nbsp;1)}.



Let E(n) be the number of subsets of M(n) which can produce the mixture with ratio (1 : 1 : 1), i.e., the mixture with equal parts A, B and C. 

We can verify that E(1) = 103, E(2) = 520447, E(10)&nbsp;mod&nbsp;118 = 82608406 and E(500)&nbsp;mod&nbsp;118 = 13801403.

Find E(10&nbsp;000&nbsp;000)&nbsp;mod&nbsp;118.
'''