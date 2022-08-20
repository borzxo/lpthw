def while_loop(increment, number):
    i = 0
    numbers = []
    while i < number:
        print(f"В начале значение i равно {i}")
        numbers.append(i)

        i += increment
        print("Текущие значения:", numbers)
        print(f"В конце значение i равно {i}")

    print("Значения: ")
    for num in numbers:
        print(num)

while_loop(3, 60)
