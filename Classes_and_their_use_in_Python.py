class Animal:
    living = True
    cry = ''

    def __init__(self):
        self.can_fly = False
        self.can_run = False

    def give_meat(self):
        print('Можно пустить на мясо')


class Bird(Animal):
    def __init__(self):
        self.can_fly = True
        self.can_run = False


class Mammal(Animal):
    def __init__(self):
        self.can_run = True
        self.can_fly = False


class Cow(Mammal, Animal):
    cry = "Muuu"

    def give_milk(self):
        print('Корова дает молоко')


class Goat(Mammal):
    cry = "Beee"

    def give_goat_milk(self):
        print('Коза дает козье молоко')


class Sheep(Mammal):
    cry = "Meee"

    def give_wool(self):
        print('Овца дает шерсть')


class Pig(Mammal):
    cry = "Hriuuu"

    def give_meat(self):
        print('Свинья дает много мяса')


class Duck(Bird):
    cry = "Kriaa"

    def give_duck_fluff(self):
        print('Утка дает утиное перо')


class Chicken(Bird):
    cry = "Co-co-co"

    def give_eggs(self):
        print('Курица дает яица')


class Goose(Bird):
    cry = "Ga-ga-ga"

    def give_goose_fluff(self):
        print('Гусь дает гусиное перо')


Zorca = Cow()
Boris = Pig()
Ivan = Goose()
Mashka = Goat()


print(Zorca.give_milk())
print(Boris.can_run)
print(Mashka.cry)
print(Ivan.living)
print(Boris.give_meat())