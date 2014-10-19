'''
If we are presented with the first k terms of a sequence it is impossible to say with certainty the value of the next term, as there are infinitely many polynomial functions that can model the sequence.

As an example, let us consider the sequence of cube numbers. This is defined by the generating function, un = n3: 1, 8, 27, 64, 125, 216, ...

Suppose we were only given the first two terms of this sequence. Working on the principle that &quot;simple is best&quot; we should assume a linear relationship and predict the next term to be 15 (common difference 7). Even if we were presented with the first three terms, by the same principle of simplicity, a quadratic relationship should be assumed.

We shall define OP(k, n) to be the nth term of the optimum polynomial generating function for the first k terms of a sequence. It should be clear that OP(k, n) will accurately generate the terms of the sequence for n &le; k, and potentially the first incorrect term (FIT) will be OP(k, k+1); in which case we shall call it a bad OP (BOP).

As a basis, if we were only given the first term of sequence, it would be most sensible to assume constancy; that is, for n &ge; 2, OP(1, n) = u1.

Hence we obtain the following OPs for the cubic sequence:







OP(1, n) = 1

1, 1, 1, 1, ...





OP(2, n) = 7n&minus;6

1, 8, 15, ...





OP(3, n) = 6n2&minus;11n+6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

1, 8, 27, 58, ...





OP(4, n) = n3

1, 8, 27, 64, 125, ...
'''