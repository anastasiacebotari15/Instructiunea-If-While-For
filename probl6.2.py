#b)S1=3((1^2)+(2^2)+...+(n^2)) si S2=(n^3)+(n^2)+(1+2+...+n)
n=int(input("n="))
s1=0
s2=0
p=0
k=0
for i in range(1,n+1):
    p+=(i**2)
    s1=3*p
    k+=i
    s2=n**3+n**2+k
if s1>s2:
    print("s1 este mai mare decat s2")
if s2>s1:
    print("s2 este mai mare decat s1")
else:
    print("s1=s2")