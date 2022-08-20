class Animal(object):

    def __init__(self, name):
        self.name = name

    def sound(str):
        print("Звуки животных")

    def __repr__(self):
        return self.pet_name

class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name)

    def sound(str):
        print("Собака: ГАВ!")

class Cat(Animal):

    def __init__(self, name):
        super(Cat, self).__init__(name)

    def sound(str):
        print("Кошка: МЯУ!")

class Person(object):

    def __init__(self, name):
        self.name = name
        self.pet = None

barsik = Dog("Барсик")
barsik.sound()
barbos = Cat("Барбос")
sharik = Cat("Шарик")
barbos.sound()
Albert = Person("Альберт")
Albert.pets = ["Барбос", "Шарик", "Барсик"]
Albert.pets = {"Кошки": ["Барбос", "Шарик"], "Собаки" : ["Барсик"]}
print("Количество питомцев Альберта: ")
for x,y in Albert.pets.items():
    print(x, ":", y)
