# похоже на сценарии с argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ок, здесь вместо *args мы делаем слудующее
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# принимает только один аргумент
def print_one(arg1):
    print(f"arg1: {arg1}")

# не принимает аргументов
def print_none():
    print("I got nothing!")


print_two("Mikhail", "Rightman")
print_two_again("Mikhail", "Rightman")
print_one("First!")
print_none()
