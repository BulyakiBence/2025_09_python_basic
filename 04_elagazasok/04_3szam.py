"""
4️ Három szám közül a legnagyobb
Kérj be három egész számot, és írd ki, melyik a legnagyobb.

"""
szam1 = int(input('Adj meg egy egesz szamot: '))
szam2 = int(input('Adj meg egy masodikat: '))
szam3 = int(input('Add meg harmadikat: '))
if szam1>szam2 and szam1 > szam3:
    print('az elso a legnagyobb')
elif szam2>szam1 and szam2 >szam3:
    print('a masodik szam a legnagyobb')
elif szam3>szam1 and szam3 >szam2:
    print('a harmadik szam a legnagyobb')