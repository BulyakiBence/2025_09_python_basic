"""
1.1 Feladat
Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e! A válasz kétféle lehet: igen vagy nem. A választól függően írjon ki üzenetet a gép!
"""
hangulat= str(input('Jó napod volt-e: '))
if hangulat == 'igen':
    print('Örülök, nekem is!')
elif hangulat== 'nem':
    print('Sajnálom, tudok segíteni ?')    