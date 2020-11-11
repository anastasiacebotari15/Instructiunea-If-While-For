#Se dau numerele naturale m si n , unde m<n. Sa se verifice daca n este o putere a lui m.
from math import log
m=int(input("introduceti m:"))
n=int(input("introduceti n:"))
i= log(n,m)
l=int(i)
if i-l==0:
    print(n, " este puterea lui ", m)
else:
    print(n ," nu este putere a lui ", m)