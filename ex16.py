from sys import argv

script, filename = argv

txt = open(filename).read()

print(f"Я собираюсь стереть файл {filename}.")
print("Если вы не хотите стирать его, нажмите сочетание клавиш CTRL+C (^C.)")
print("Если хотите стереть файл, нажмите клавишу Enter.")

input("?")

print("Открытие файла...")
target = open(filename, 'w')

print("Очистка файла. До свидания!")


print("Теперь я запрашиваю у вас три строки.")

line1 = input("строка 1: ")
line2 = input("строка 2: ")
line3 = input("строка 3: ")

print("Это я запишу в файл")

target.write(f"\n{line1}" f"\n {line2}" f"\n{line3}")


print("И наконец, я закрою файл.")
target.close()
