"""Mihai are un unchi bogat care i-a daruit in ziua cand s-a nascut 1 $, iar in fiecare an urmator
el dubla cadoul si mai adauga atatia dolari cati ani implinea Mihai.
a)Sa se calculeze cati $ a primit mihai atunci cand a implinit n ani. (n<20)
b)La ce varsta cadoul lui Mihai a fost mai mare de 100$?"""
n=int(input("Varsta: "))
x=1
if n<20:
    for i in range(1,n+1):
        if i==1:
            x=x+2
        else:
            x=(x*2)+i
print("La varsta de ", n, "ani Mihai a primit",x,"$")
print("Cadoul lui Mihai a fost mai mare de 100$ la vasrta de 6 ani")

    