'''
 Set je množina jedinečných hodnot
 Množina je neuspořádaná a neindexovaná kolekce.
 V jazyce Python se množiny zapisují pomocí složených závorek.
'''
my_set = {2, 3, 9, 7}
print('Množina my_set: ', my_set)
print('Typ my_set: ', type(my_set))

# Vytvoření množiny ze seznamu hodnot (list)
numbers = [1, 4, 1, 5, 3, 3, 1, 2, 8, 2]
print(f'Proměnná numbers - seznam (list): {numbers}')
set_numbers = set(numbers)
print(f'Proměnná set_numbers - množina (set): {set_numbers}')

# Vytvoření množiny jedinečných znaků z řetězce
chars = sorted(list('Hello world'))
set_chars = set(chars)
print(f'Uspořádaná množina (set) jedinečných hodnot: {set_chars}')

# Jakmile je sada vytvořena, nemůžete její položky měnit, ale můžete přidávat nové položky.
# Pro přidání jedné položky do sady použijte metodu add().
set_chars.add('V')

# Chcete-li do sady přidat více než jednu položku, použijte metodu update().
set_chars.update('X', 'Y', 'Z')

# Chcete-li odstranit položku z množiny, použijte metodu remove() nebo discard().
set_chars.remove('H')
print(f'Proměnná set_chars: {set_chars}')

# Metoda clear() vyprázdní množinu
set_chars.clear()

# Klíčové slovo del sadu zcela odstraní:
del set_chars

# Přístup k hodnotám množiny
# K položkám v množině nelze přistupovat odkazem na index, protože množiny jsou neuspořádané, položky nemají žádný index.
# my_set[1]

# Položky množiny však můžete procházet pomocí cyklu for nebo se pomocí klíčového slova in zeptat, zda se zadaná hodnota v množině vyskytuje.
for x in my_set:
  print(x)

'''
Množinové operace
'''
# Sjednocení množin
print(f'set_numbers | my_set: {set_numbers | my_set}')
print(f'set_numbers.union(my_set): {set_numbers.union(my_set)}')
# Průnik množin
print(f'set_numbers & my_set: {set_numbers & my_set}')
print(f'set_numbers.intersection(my_set): {set_numbers.intersection(my_set)}')
# Rozdíl množin
print(f'set_numbers - my_set: {set_numbers - my_set}')
print(f'set_numbers.difference(my_set): {set_numbers.difference(my_set)}')
# Doplněk množin
print(f'set_numbers ^ my_set: {set_numbers ^ my_set}')
print(f'set_numbers.symmetric_difference(my_set): {set_numbers.symmetric_difference(my_set)}')
# Zjištění zda množina obsahuje hodnotu
print(f'1 in set_numbers: {1 in set_numbers}')
