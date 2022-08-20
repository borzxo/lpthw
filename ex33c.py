def range_loop(number):
    numbers = []
    for number in range(0, 60):
        print(f"Значение числа: {number}")
        numbers.append(number)

    print("Значения чисел: ")
    for num in numbers:
        print(num)

range_loop(60)
