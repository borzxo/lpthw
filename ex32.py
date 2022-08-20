the_count = [1, 2 , 3, 4, 5]
fruits = ['apple', 'orange', 'peach', 'apricot']
change = [1, 'chervonets', 2, 'poltinnik', 3, 'sotnya']

# цикл for первого типа обрабатывает список
for number in the_count:
    print(f"Schetchik {number}")

# то же, что и выше
for fruit in fruits:
    print(f"Fruit {fruit}")

# также можно обрабатывать смешанные списки
# обратите винимание, что используются символы {}, так как неизвестен
# тип значения
for i in change:
    print(f"I kept {i}")

# также мы можем создавать списки, начнем с пустого
elements = []

# затем используется функция range() для ограничения диапазона
for i in range(0, 10):
    print(f"Adding {i} to the list.")
    # append - функция для добавления элементов в список
    elements.append(i)

# теперь мы их выводим
for i in elements:
    print(f"Number of the element: {i}")
