#
# CS1010X --- Programming Methodology
#
# Mission 15 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games_classes import *
from engine import *
import simulation
import random

# Rename XX_AI to YourName_AI
class Ivan_AI(Tribute):
    def next_action(self):
        # Next action should return a tuple of what your next action should
        # be. For the full list of tuple that your AI can return, refer to
        # the pdf file

        # As an example: the following code will make your AI just walk around
        # randomly every turn. You do NOT have to use this code if you don't
        # want to!
        things_around = self.objects_around()
##        print("things",things_around)
        owned = self.get_inventory()
##        print("owned",owned)
        possible_food = []
        possible_animals = []
        possible_weapons = []
        possible_ammo = []
        tributes = []
        # sort out what is available in tile
        for thing in things_around:
            if type(thing) == Animal:
                possible_animals.append(thing)
            elif isinstance(thing, Food) and not thing.is_owned():
                possible_food.append(thing)
            elif isinstance(thing, Weapon) and not thing.is_owned():
                possible_weapons.append(thing)
            elif isinstance(thing, Ammo) and not thing.is_owned():
                possible_ammo.append(thing)
            elif isinstance(thing, Person):
                tributes.append(thing)

        # sort items to use
        ranged = list(filter(lambda x: type(x) == RangedWeapon, owned))
        ranged.sort(key = lambda x: x.max_damage(), reverse = True)
        ammos = list(filter(lambda x: type(x) == Ammo, owned))
        melee = list(filter(lambda x: type(x) == Weapon, owned))
        melee.sort(key = lambda x: x.max_damage(), reverse = True)
        all_loaded_weapons = list(filter(lambda x: x.shots_left() > 0 if type(x) == RangedWeapon else True ,filter(lambda x: isinstance(x, Weapon),owned)))
        all_loaded_weapons.sort(key = lambda x: x.max_damage(), reverse = True)
        to_eat = list(self.get_food())
        to_eat.sort(key = lambda x: x.get_food_value(), reverse = True)
        meds = list(self.get_medicine())
        meds.sort(key = lambda x: x.get_medicine_value(), reverse = True)
        
        
        # if i have a weapon and is see a tribute, attack them
        if len(all_loaded_weapons) > 0 and len(tributes) > 0:
            tributes.sort(key = lambda x: x.get_health(), reverse = False) # sort tributes byv lowest health
            return ("ATTACK", tributes[0],all_loaded_weapons[0])

        # if less than 60% hunger and no one around eat food
        elif self.get_hunger() >= 40 and len(to_eat) > 0 and len(tributes) == 0:
            return ("EAT", to_eat[0])

        # if damaged and no one around heal up
        elif self.get_health() < 100 and len(meds) > 0 and len(tributes) == 0:
            return ("EAT", meds[0])
        
        # there is an empty ranged weapon, load it
        if len(ranged) > 0: 
            for wea in ranged:
                if wea.shots_left() == 0:
                    for ammo in ammos:
                        if ammo.weapon_type() == wea.get_name():
                            return ("LOAD", wea, ammo)

        #  there is an unpicked weapon and it is better than mine then take it
        if len(possible_weapons) > 0:
            best = possible_weapons[0]
            for weapon in possible_weapons:
                if weapon.max_damage() > best.max_damage() and (weapon.min_damage() - best.min_damage()) >= 0:
                    best = weapon
            if type(best) == Weapon:
                if len(melee)==0 or best.max_damage() > melee[0].max_damage():
                    return("TAKE", best)
            elif type(best) == RangedWeapon:
                if len(ranged)==0 or  best.max_damage() > ranged[0].max_damage():
                    return("TAKE", best)
        
        # if the unpicked ammo is for my weapon pick it up
        if len(possible_ammo) > 0:
            for ammo in possible_ammo:
                if ammo.weapon_type() in map(lambda x: x.get_name(),filter(lambda x:type(x) == RangedWeapon,owned)):
                    return("TAKE", ammo)
                
        # if there is food pick it up
        if len(possible_food) > 0:
            ffood = possible_food[0]
            for food in possible_food:
                if food.get_food_value() > ffood.get_food_value():
                    ffood = food
            return("TAKE", ffood)

        # if there are animals, kill them if i have a weapon
        if len(possible_animals) > 0 and len(all_loaded_weapons) > 0:
            fanimal = possible_animals[0]
            for animal in possible_animals:
                if animal.get_food_value() > fanimal.get_food_value():
                    fanimal = animal
            return("ATTACK", fanimal, all_loaded_weapons[0])
                                                            
        
        exits = self.get_exits()
        if exits:
            index = random.randint(0, len(exits)-1)
            direction = exits[index]
            return ("GO", direction)

        # Otherwise, do nothing
        return None


# NOTE: DO NOT remove the 2 lines of code below.
#
# In particular, you will need to modify the `your_AI = XX_AI` line so that
# `XX_AI` is the name of your AI class.
# For instance, if your AI class is called `MyPrecious_AI`, then you have to
# modify that line to:
#
#     your_AI = MyPrecious_AI
#
# Failure to do so will result in the following exception on Coursemology when
# you run the test cases:
#
#     Traceback (most recent call last):
#       in <module>
#     NameError: name 'your_AI' is not defined
#
# You have been warned!
time_limit = 50 # Modify if your AI needs more than 50 moves for task 2
your_AI = Ivan_AI # Modify if you changed the name of the AI class



##################
# Simulation Code
##################
##########
# Task 1 #
##########
# Goal:
# 1. Your AI should be able to pick up a Weapon / RangedWeapon
# 2. Your AI should be able to kill chicken
# 3. Your AI should be able to pick up chicken_meat after killing chicken

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI
##simulation.task1(Ivan_AI("Ivan AI", 100), gui=True)


##########
# Task 2 #
##########
## 1. Your AI should be able to pick up a Weapon / RangedWeapon
## 2. Your AI should be able to move around and explore
## 3. Your AI should be able to find harmless Tribute and kill him

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI

time_limit = 20    # You may change the time limit if your AI is taking too long
##simulation.task2(Ivan_AI("Ivan AI", 100), time_limit, gui=True)



#################
# Optional Task
#################
## You can create your own map and see how your AI behaves!

# Define the parameters of the map
def config():
    ## The game should have a 3x3 map
    game_map = GameMap(4)

    ## You can change the numbers to create different kinds of maps for
    ## the optional task.
    game_config = GameConfig()
    game_config.set_item_count(Weapon, 5)
    game_config.set_item_count(Animal, 10)
    game_config.set_item_count(RangedWeapon, 5)
    game_config.set_item_count(Food, 5)
    game_config.set_item_count(Medicine, 5)

    game = GameEngine(game_map, game_config)

    # Add some dummy tributes
    ryan = Tribute("Ryan", 100)
    waihon = Tribute("Wai Hon", 100)
    soedar = Tribute("Soedar", 100)

    game.add_tribute(ryan)
    game.add_tribute(waihon)
    game.add_tribute(soedar)

    # Yes, your AI can fight with himself
    ai_clone = Ivan_AI("AI Clone", 100)
    game.add_tribute(ai_clone)
    ai_clone2 = Ivan_AI("AI 2 Clone", 100)
    game.add_tribute(ai_clone2)

    return game

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI
simulation.optional_task(Ivan_AI("Ivan AI", 100), config, gui=False)
