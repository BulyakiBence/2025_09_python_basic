"""
2. Feladat
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!
"""
import random
# 1 =='fej'
# 2 == 'írás'
fej = 1
írás = 2
x = random.randint(1,2)
coinflip = int(input(f'Válassz! Fej(1) vag írás(2): '))
if coinflip == x:
    print('Eltaláltad!')
else: 
    print('Sajnos ez most nem sikerült')