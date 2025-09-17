# szam = int(input ("Adj meg egy számot: "))
# if szam < 0:
#     print('Az adott szám negatív')
# elif szam > 0:
#     print('pozitív')
# else:
#     print('Nulla')

"Páros számra írja ki a program azt, hogy páros, a páratlanra azt, hogy páratlan."    

szam = int(input('Adj meg egy szamot'))

if szam % 2 == 0 and szam != 0:
    print('Páros')
elif szam ==0:
    print('Nulla')
else:
    print('Páratlan')    