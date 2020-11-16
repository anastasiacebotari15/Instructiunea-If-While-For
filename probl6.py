#Se da numarul natural n.Sa se compare sumele S1 si S2, unde:
#a)S1=(1^3)+ (2^3)+...+(n^3) si S2=(1+2+...+n)^2
#b)S2=3((1^2)+(2^2)+...+(n^2)) si S2=(n^3)+(n^2)+(1+2+...+n)
n=int(input("Intrpduceti n : "))
s1=0
s2=0
p=0
for i in range(1,n+1):
    s1+=i**3
    p+=i
    s2=p**2
if s1>s2:
    print("s1 este mai mare decat s2")
if s2>s1:
    print("s2 este mai mare decat s1")
else:
    print("s1=s2")