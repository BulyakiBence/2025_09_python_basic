""""
B csoport:
Készítsünk programot, amely segíti a burkoló mesterek munkáját.
A szükséges csempe mennyiségének a kiszámításához a program kérje be a terület szélességét és a magasságát centiméterben,
valamint, hogy hány darab csempét vásároltunk már, majd számolja ki a területét (a*b), és
hogy a 20cm*20cm méretű csempék esetén hány darabra van szükség a munka elvégzéséhez (a plusz 10%-ot az illesztések miatt illik rászámolnunk).
A program azt is állapítsa meg, és közölje a felhasználóval, hogy kell-e még vásárolnunk csempét!
"""

magassag = int(input('Add meg a magasságot (cm): '))
szelesseg = int (input('Add meg a szelesseget (cm): '))
csempe = int(input('Eddig vásárolt csempék száma: '))
terulet = szelesseg * magassag 
print (f'A területük {terulet}')
egycsempe = 20*20
szukseg = (terulet/egycsempe) * 1.1
print(f'Ennyi csempe kell {szukseg}')
if csempe < szukseg :
    print('Nem lesz elég, kell még csempe')
else:
    print('Elég lesz a csempe')


