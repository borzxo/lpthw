def while_loop(number):
    i = 0
    numbers = []
    while i < number:
        print(f"В начале значение i равно {i}")
        numbers.append(i)

        i += 1
        print("Текущие значения:", numbers)
        print(f"В конце значение i равно {i}")

while_loop(3)
while_loop(15)
