'''
Tuples - neměnitelné n-tice hodnot (seřazený seznam prvků)
In Python tuples are written with round brackets.
'''

# Vytvoření tuples
numbers = (1, 2, 3)
print('numbers: ', numbers)
print('Type(numbers): ',type(numbers))

chars = tuple('Hello world')
print('chars: ', chars)
print('Type(chars): ',type(chars))

# Chcete-li vytvořit tuple s jedinou položkou, musíte za položku přidat čárku, jinak Python proměnnou jako tuple nerozpozná.
colors = ('red',)
print('colors: ', colors)

# Součet tuples
print(f'chars + numbers: {chars + numbers}')

# Výpis hodnot 
# Rozsah indexů můžete zadat tak, že určíte, kde má rozsah začínat a kde končit.
# Při zadání rozsahu bude návratovou hodnotou nový tuple se zadanými položkami.
print(f'chars[2:5]: {chars[2:5]}')

# Záporné indexování znamená, že se začíná od konce, -1 označuje poslední položku, -2 označuje předposlední položku atd.
# Pokud chcete začít hledat od konce tuplu, zadejte záporné indexy:
# Tento příklad vrátí položky od indexu -4 (zahrnuto) do indexu -1 (vyloučeno).
print(f'chars[-4:-1]: {chars[-4:-1]}')

# Chcete-li zjistit, kolik položek má tuple, použijte metodu len():
print(f'len(chars): {len(chars)}')

# Zjištění prvního výskytu a počtu výskytu prvku
if 'l' in chars:
    print(f'chars.index("l"): {chars.index("l")}')
    print(f'chars.count("l"): {chars.count("l")}')

# Záměna hodnot proměnných
x = 10
y = 2
x, y = y, x
print(f'x: {x}, y: {y}')
