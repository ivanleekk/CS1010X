class Food:
    def __init__(self, name, nutrition, good_until):
        self.name = name
        self.nutrition = nutrition
        self.good_until = good_until
        self.age = 0
        pass

    def sit_there(self, time):
        self.age += time
        pass

    def eat(self):
        if self.age <= self.good_until:
            return self.nutrition
        else:
            return 0


class AgedFood(Food):
    def __init__(self, name, nutrition, good_until, good_after):
        super.name = name
        super.nutrition = nutrition
        super.good_until = good_until
        self.good_after = good_after
        pass

    def sniff(self):
        if super.age > self.good_after:
            return True
        else:
            return False

    def eat(self):
        if super.age < self.good_after:
            return 0
        else:
            return super.nutrition


class VendingMachine:
    def __init__(self, name, nutrition, good_until):
        self.name = name
        self.nutrition = nutrition
        self.good_until = good_until
        self.age = 0
        pass

    def sit_there(self, time):
        self.age += time / 2
        pass

    def sell_food(self):
        food = Food(self.name, self.nutrition, self.good_until)
        food.age = self.age
        return food


FR = Food("Fried Rice", 50, 40)
print(FR.eat())
FR.sit_there(10)
print(FR.eat())
FR.sit_there(10)
print(FR.eat())
FR.sit_there(10)
print(FR.eat())
FR.sit_there(10)
print(FR.eat())
FR.sit_there(10)
print(FR.eat())
FR.sit_there(10)
print(FR.eat())
FR.sit_there(10)
