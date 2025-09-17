"""
6️ Egyszerű jelszóellenőrző
Kérj be egy jelszót, és ha megegyezik a „titok” szóval, írd ki: „Belépés engedélyezve!”, különben „Helytelen jelszó!”.
"""
jelszo = str(input('Adj meg egy jelszót: '))
if jelszo == ('titok'):
    print('Belépes engedélyezve')
else:
    print('Helytelen jelszó')