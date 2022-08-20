def add(a, b):
    print(f"Сложение {a} + {b}")
    return a + b

def substract(a, b):
    print(f"Вычитание {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Умножение {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Деление {a} / {b}")
    return a / b


print("Давайте выполним несколько вычислений с помощью функций!")

age = add(float(input()) , float(input()))
height = substract(190, 4)
weight = multiply(35, 2)
iq = divide(250, 2)

print(f"Возраст: {age}, Рост: {height}, Вес: {weight}, IQ: {iq}")


# Головоломка в качестве дополнительного задания, введите код в любом случае.
print("Это головоломка.")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print("Получается: ", what, "Вы можете это вычислить вручную?")
# 35 + (186 - (70 * (125 / 2)))

# age * (10 + 3)
output = multiply(age, add(10, 3))
print(f"Output: {output}")
