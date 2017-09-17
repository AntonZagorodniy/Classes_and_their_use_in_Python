class Animal:
    living = True
    cry = ''

    def __init__(self):
        self.name = ''

    def give_meat(self):
        print('Можно пустить на мясо')


class Bird(Animal):
    can_fly = True


class Mammal(Animal):
    can_run = True


class Cow(Mammal, Animal):
    cry = "Muuu"

    def give_milk(self):
        print('{} дает молоко'. format(self.name))


class Goat(Mammal):
    cry = "Beee"

    def give_goat_milk(self):
        print('{} дает козье молоко'. format(self.name))


class Sheep(Mammal):
    cry = "Meee"

    def give_wool(self):
        print('{} дает шерсть'. format(self.name))


class Pig(Mammal):
    cry = "Hriuuu"

    def give_meat(self):
        print('{} дает много мяса'. format(self.name))


class Duck(Bird):
    cry = "Kriaa"

    def give_duck_fluff(self):
        print('{} дает утиное перо'. format(self.name))


class Chicken(Bird):
    cry = "Co-co-co"

    def give_eggs(self):
        print('{} дает яица'. format(self.name))


class Goose(Bird):
    cry = "Ga-ga-ga"

    def give_goose_fluff(self):
        print('{} дает гусиное перо'. format(self.name))


cow_1 = Cow()
cow_1.name = 'Зорька'

pig_1 = Pig()
pig_1.name = 'Борис'

goose_1 = Goose()
goose_1.name = 'Иван'

goat_1 = Goat()
goat_1.name = 'Машка'


print(cow_1.give_milk())
print(pig_1.can_run)
print(goat_1.cry)
print(goose_1.living)
print(pig_1.give_meat())