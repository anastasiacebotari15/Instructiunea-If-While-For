"""Un numar natural se numeste numar perfect daca este egal cu suma divizorilor lui,in afara de 
el insusi. De exemplu, numarul 6 este numar perfect, deoarece 6=1+2+3.Sa se afle numerele perfecte 
mai mici decat numarul natural dat n."""
n = int(input("Introdu un numar n: "))
s = 0
for i in range(1, n):
    if(n % i == 0):
        s =s + i
if (s == n):
    print(n, "este un numar perfect")
else:
    print(n, "nu este numar perfect")