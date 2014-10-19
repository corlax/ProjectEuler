'''
table.p375 td {

  padding: 0px 3px 0px 3px;

  vertical-align: bottom;

  text-align: left;

}



Let Sn be an integer sequence produced with the following pseudo-random number generator:



  

    S0

    =&nbsp;

    290797&nbsp;

  

    Sn+1

    =&nbsp;

    Sn2 mod 50515093

  







Let A(i, j) be the minimum of the numbers Si, Si+1, ... , Sj for i &le; j.

Let M(N) = &Sigma;A(i, j) for 1 &le; i &le; j &le; N.

We can verify that M(10) = 432256955 and M(10 000) = 3264567774119.





Find M(2 000 000 000).
'''