import random
data = [
    (x * 3 if x % 2 == 0 else x * 5 / 2)
    for i, x in enumerate([random.randint(1, 100) for i in range(42)])
    if (i + 1) % 5 != 0
]
print(f'A listában 42 db random szám szerepel 1 és 100 között, amelyek közült minden páros számot megszoroz 3-mal, minden páratlant megszoroz 5-tel és oszt 2-vel. Minden 5. számot kivesz.')
print(f'A lista: {data}')
user_szam = int(input("Adj meg egy kétjegyű számot!"))
print(f'Az új lista: {data.insert(1, user_szam)}')
user_szam_remove = int(input("Adj meg egy számot a listából, amit törölni szeretnél!"))
print(f'A lista a törlés után: {data.remove(user_szam_remove)}')
print(f'Sorbarendezve a lista számait: {data.sort()}')
print(f'Visszafelé rendezve a lista számait: {data.reverse()}')
