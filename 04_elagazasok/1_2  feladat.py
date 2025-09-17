"""
1.2 Feladat
Fejleszd tovább az első feladat programját úgy, hogy amennyiben a felhasználó nem a két lehetséges válasz (igen/nem) közül ad meg egyet, a gép kiírja: "Sajnos nem értem a válaszodat!"
"""
hangulat= str(input('Jó napod volt-e: '))
if hangulat == 'igen':
    print('Örülök, nekem is!')
elif hangulat== 'nem':
    print('Sajnálom, tudok segíteni ?')    
else:
    print('Sajnos nem értem a válaszodat')