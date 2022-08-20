
class Animal(object):
    pass

class Dog(Animal):

    def __init__(self, name):
        self.name = name

    def pet_name(self):
        name = f"Эту собаку зовут {self.name}."
        print(name)

    def count_letters(self):
        count = f"Имя этой собаки состоит из {len(self.name)} букв.\n"
        print(count)

class Cat(Animal):

    def __init__(self, name):
        self.name = name

    def pet_name(self):
        name = f"Эту кошку зовут {self.name}."
        print(name)

    def count_letters(self):
        count = f"Имя этой кошки состоит из {len(self.name)} букв.\n"
        print(count)

class Person(object):

    def __init__(self, name):
        self.name = name

    def first_name(self):
        print(f"Этого человека зовут {self.name}.")

    def count_letters(self):

        print(f"Имя этого человека состоит из {len(self.name)} букв.\n")

barsik = Dog("Барсик")
barsik.pet_name()
barsik.count_letters()

barbos = Cat("Барбос")
barbos.pet_name()
barbos.count_letters()

albert = Person("Альберт")
albert.first_name()
albert.count_letters()
