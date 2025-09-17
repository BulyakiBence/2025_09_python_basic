"""
3️ Jegyosztályozás
Kérj be egy pontszámot 0–100 között, és írd ki az érdemjegyet:
0–49: Elégtelen


50–64: Elégséges


65–79: Közepes


80–89: Jó


90–100: Jeles

"""
pontszam = int(input('Adj megy egy pontszamot: '))
if pontszam <=100 and pontszam >=90:
    print('5-ös lett!')
elif pontszam <=89 and pontszam  >=80:
    print('4es')    
elif pontszam <=79 and pontszam  >=65:
    print('3as')
elif pontszam <=64 and pontszam  >=50:
    print('2-es')
elif pontszam<=49 and pontszam >=0:
    print('1-es')
else:
    print('Nem lehetséges')