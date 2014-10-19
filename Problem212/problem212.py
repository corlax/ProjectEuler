'''
An axis-aligned cuboid, specified by parameters { (x0,y0,z0), (dx,dy,dz) }, consists of all points (X,Y,Z) such that x0 &le; X &le; x0+dx, y0 &le; Y &le; y0+dy and z0 &le; Z &le; z0+dz.  The volume of the cuboid is the product, dx &times; dy &times; dz.  The combined volume of a collection of cuboids is the volume of their union and will be less than the sum of the individual volumes if any cuboids overlap.



Let C1,...,C50000 be a collection of 50000 axis-aligned cuboids such that Cn has parameters



x0 = S6n-5 modulo 10000y0 = S6n-4 modulo 10000z0 = S6n-3 modulo 10000dx = 1 + (S6n-2 modulo 399)dy = 1 + (S6n-1 modulo 399)dz = 1 + (S6n modulo 399)



where S1,...,S300000 come from the &quot;Lagged Fibonacci Generator&quot;:



For 1 &le; k &le; 55, Sk = [100003 - 200003k + 300007k3] &nbsp; (modulo 1000000)For 56 &le; k, Sk = [Sk-24 + Sk-55] &nbsp; (modulo 1000000)



Thus, C1 has parameters {(7,53,183),(94,369,56)}, C2 has parameters {(2383,3563,5079),(42,212,344)}, and so on.



The combined volume of the first 100 cuboids, C1,...,C100, is 723581599.



What is the combined volume of all 50000 cuboids, C1,...,C50000 ?
'''