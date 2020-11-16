"""Conform calendarului japonez fiecare an poarta numele unui animal.Fiecare denumire se repeta
exact la 12 ani.Deci, un ciclu este format din 12 ani cuurmatoarele denumiri de animale in 
aceasta ordine:sobolan,bou,tigru,iepure,dragon,sarpe,cal,oaie,maimuta,cocos,caine,porc. Stiind
Stiind ca anul 2000 a fost anul dragonului, sa se scrie un algoritm care va citi de la tastatura
anul(numarul e patru cifre) si va afisa denumirea lui conform calendarului japonez."""
i=int(input("Introduceti anul: "))
if i%12==8:
    print("Dragon")
if i%12==7:
    print("Iepure")
if i%12==6:
    print("Tigru")
if i%12==5:
    print("Bou")
if i%12==4:
    print("Sobolan")
if i%12==9:
    print("Sarpe")
if i%12==10:
    print("Cal")
if i%12==11:
    print("Oaie")
if i%12==0:
    print("Maimuta")
if i%12==3:
    print("Porc")
if i%12==2:
    print("Caine")
if i%12==1:
    print("Cocos")