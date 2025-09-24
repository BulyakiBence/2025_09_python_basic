""""
1. Feladat
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót!
"""
import random
x = random.randint(1,3)
szam = int(input('Adj meg eg számot 1 és 3 között: '))
if szam == x:
    print('Erre a számra gondoltam, ügyes vagy!')
elif szam < x:
    print('Nagyobb számra gondoltam')
elif szam > x:
    print('Kisebb számra gondoltam')