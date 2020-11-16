#Sa se scrie un program care va efectua :
#a)adunarea a doua fractii
#b)imnultirea a doua fractii
#Rezultatul va fi o fractie ireductibila
from fractions import Fraction
m=int(input("numaratorul primei fractii:"))
n=int(input("numitorul primei fractii:"))
l=int(input("numaratorul la a doua fractie:"))
i=int(input("numitorul la a doua fractie:"))
print("Suma= ",Fraction(m,n)+Fraction(l,i))
print("Produsul= ",Fraction(m,n)*Fraction(l,i))
