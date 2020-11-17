"""Se dau numerele pozitive a,b,c.Sa se verifice daca exista un triunghi ale carui laturi au lungimile(in aceeasi unitate de masura) egale cu a,b,c. In caz afirmativ, sa se determine tipul triunghiului:echilateral,
isoscel,scalen."""
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if (a<b+c) and (b<a+c) and (c<a+b):
    if(a==b) and (b==c) and (c==a):
        print("triunghiul este echilateral")
    if(a!=b) and (b!=c) and (c!=a):
        print("triunghiul este scalen")
    if ((a==b) and (a!=c) and(b!=c)) or ((b==c) and (b!=a) and (c!=a)) or ((c==a) and (c!=b) and (a!=b)):
        print("triunghiul este isoscel")