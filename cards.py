import random

karty = [
    ['♠', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'],
    ['♥', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'],
    ['♦', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'],
    ['♣', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']]

gracze = {}

while True:
    ilosc_graczy = int(input('Wybierz ilość graczy(2-4): '))
    if ilosc_graczy < 1 or ilosc_graczy > 4:
        print('Błędna ilość graczy!')
    else:
        break
        
# uzupełnianie nazw graczy
print('Wpiszcie swoje nazwy!')
for gracz in range(ilosc_graczy):
    nazwa = input(f'Gracz{gracz+1}: ')
    gracze[nazwa] = []

# rozdawanie kart
try:
    while True:
        licz = 0
        for kolor in range(4):
            if len(karty[kolor]) == 1:
                licz += 1

        if licz == 4:
            raise ValueError

        for klucz in gracze:
            kolor = random.randint(0, 3)
            
            licz = 0
            while len(karty[kolor]) == 1:
                kolor = (kolor + 1) % 4
                licz += 1
                if licz == 4:
                    raise ValueError
            
            karta = random.randint(1, len(karty[kolor])-1)
            gracze[klucz].append(f'{karty[kolor][0]}{karty[kolor].pop(karta)}')
except ValueError:
    for gracz in gracze:
        print(f'{gracz}: {gracze[gracz]}')
    print()
    print('T - Trefl\nP - Pik\nKa - Karo\nKi - Kier')
except Exception as e:
    print(f'Error: {e}')
