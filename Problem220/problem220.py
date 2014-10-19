'''
Let D0 be the two-letter string &quot;Fa&quot;.  For n&ge;1, derive Dn from Dn-1 by the string-rewriting rules:



&quot;a&quot; &rarr; &quot;aRbFR&quot;

&quot;b&quot; &rarr; &quot;LFaLb&quot;



Thus, D0 = &quot;Fa&quot;, D1 = &quot;FaRbFR&quot;, D2 = &quot;FaRbFRRLFaLbFR&quot;, and so on.



These strings can be interpreted as instructions to a computer graphics program, with &quot;F&quot; meaning &quot;draw forward one unit&quot;, &quot;L&quot; meaning &quot;turn left 90 degrees&quot;, &quot;R&quot; meaning &quot;turn right 90 degrees&quot;, and &quot;a&quot; and &quot;b&quot; being ignored.  The initial position of the computer cursor is (0,0), pointing up towards (0,1).



Then Dn is an exotic drawing known as the Heighway Dragon of order n.  For example, D10 is shown below; counting each &quot;F&quot; as one step, the highlighted spot at (18,16) is the position reached after 500 steps.
'''