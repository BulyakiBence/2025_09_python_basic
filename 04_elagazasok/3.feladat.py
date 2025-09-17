"""
3. Feladat
Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.


"""
import random
x = random.randint(1,5)
szam = int(input('Adj meg egy számot: '))
if szam == x:
    print('Egyenlő')
elif szam > x:
    print('Kisebb számra gondoltam:)')      
elif szam < x:
    print('Nagyobb számra gondoltam:)')