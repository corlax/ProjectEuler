'''
table.p238 td { padding: 0px 3px 0px 3px; }





Create a sequence of numbers using the "Blum Blum Shub" pseudo-random number generator:





  

    s0

    =

    14025256

  

    sn+1

    =

    sn2 mod 20300713

  





Concatenate these numbers &thinsp;s0s1s2&hellip; to create a string w of infinite length.

Then, w&thinsp;=&thinsp;14025256741014958470038053646&hellip;



For a positive integer k, if no substring of w exists with a sum of digits equal to k, p(k) is defined to be zero. If at least one substring of w exists with a sum of digits equal to k, we define p(k)&thinsp;=&thinsp;z, where z is the starting position of the earliest such substring.



For instance:



The substrings 1, 14, 1402, &hellip; 

with respective sums of digits equal to 1, 5, 7, &hellip;

start at position 1, hence p(1)&thinsp;=&thinsp;p(5)&thinsp;=&thinsp;p(7)&thinsp;=&thinsp;&hellip;&thinsp;=&thinsp;1.



The substrings 4, 402, 4025, &hellip;

with respective sums of digits equal to 4, 6, 11, &hellip;

start at position 2, hence p(4)&thinsp;=&thinsp;p(6)&thinsp;=&thinsp;p(11)&thinsp;=&thinsp;&hellip;&thinsp;=&thinsp;2.



The substrings 02, 0252, &hellip;

with respective sums of digits equal to 2, 9, &hellip;

start at position 3, hence p(2)&thinsp;=&thinsp;p(9)&thinsp;=&thinsp;&hellip;&thinsp;=&thinsp;3.



Note that substring 025 starting at position 3, has a sum of digits equal to 7, but there was an earlier substring (starting at position 1) with a sum of digits equal to 7, so p(7)&thinsp;=&thinsp;1, not 3.



We can verify that, for 0&thinsp;
'''