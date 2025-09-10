"""
Thonny fejlesztői környezetben készíts egy rövid programot, amely
kommentként tartalmazza a program funkciójának leírását,
konstansként tárolja PI értékét,
egy másik változóban tárolja egy kör sugarának nagyságát (cm-ben megadva),
kiszámolja és a képernyőre kiírja a kör kerületét és területét!
"""
PI = 3.14
radius = 5 # cm
kerulet = PI * radius * 2
terulet = radius * radius * PI
print(f'Kör kerülete:{kerulet} cm')
print(f'Kör kerülete:{terulet} cm2')