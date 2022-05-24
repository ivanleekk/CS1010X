#
# CS1010X --- Programming Methodology
#
# Contest 15.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games_classes import *
from contest_simulation import *
import random


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
        ranged.sort(key=lambda x: x.max_damage(), reverse=True)
        ammos = list(filter(lambda x: type(x) == Ammo, owned))
        melee = list(filter(lambda x: type(x) == Weapon, owned))
        melee.sort(key=lambda x: x.max_damage(), reverse=True)
        all_loaded_weapons = list(
            filter(
                lambda x: x.shots_left() > 0 if type(x) == RangedWeapon else True,
                filter(lambda x: isinstance(x, Weapon), owned),
            )
        )
        all_loaded_weapons.sort(key=lambda x: x.max_damage(), reverse=True)
        to_eat = list(self.get_food())
        to_eat.sort(key=lambda x: x.get_food_value(), reverse=True)
        meds = list(self.get_medicine())
        meds.sort(key=lambda x: x.get_medicine_value(), reverse=True)

        # if i have a weapon and is see a tribute, attack them, unless they have more health than me then run
        if len(all_loaded_weapons) > 0 and len(tributes) > 0:
            tributes.sort(
                key=lambda x: x.get_health(), reverse=False
            )  # sort tributes byv lowest health
            if tributes[0].get_health() <= self.get_health():
                return ("ATTACK", tributes[0], all_loaded_weapons[0])
            else:
                exits = self.get_exits()
                if exits:
                    index = random.randint(0, len(exits) - 1)
                    direction = exits[index]
                    return ("GO", direction)

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
                if (
                    weapon.max_damage() > best.max_damage()
                    and (weapon.min_damage() - best.min_damage()) >= 0
                ):
                    best = weapon
            if type(best) == Weapon:
                if len(melee) == 0 or best.max_damage() > melee[0].max_damage():
                    return ("TAKE", best)
            elif type(best) == RangedWeapon:
                if len(ranged) == 0 or best.max_damage() > ranged[0].max_damage():
                    return ("TAKE", best)

        # if the unpicked ammo is for my weapon pick it up
        if len(possible_ammo) > 0:
            for ammo in possible_ammo:
                if ammo.weapon_type() in map(
                    lambda x: x.get_name(),
                    filter(lambda x: type(x) == RangedWeapon, owned),
                ):
                    return ("TAKE", ammo)

        # if there is food pick it up
        if len(possible_food) > 0:
            ffood = possible_food[0]
            for food in possible_food:
                if food.get_food_value() > ffood.get_food_value():
                    ffood = food
            return ("TAKE", ffood)

        # if there are animals, kill them if i have a weapon
        if len(possible_animals) > 0 and len(all_loaded_weapons) > 0:
            fanimal = possible_animals[0]
            for animal in possible_animals:
                if animal.get_food_value() > fanimal.get_food_value():
                    fanimal = animal
            return ("ATTACK", fanimal, all_loaded_weapons[0])

        exits = self.get_exits()
        if exits:
            index = random.randint(0, len(exits) - 1)
            direction = exits[index]
            return ("GO", direction)

        # Otherwise, do nothing
        return None


# #######################################
# # Testing Code
# #######################################

# # We only execute code inside the if statement if this file is
# # not being imported into another file
# if __name__ == "__main__":

#     def qualifer_map(size, wrap):
#         game_config = GameConfig()
#         game_config.set_item_count(Weapon, 10)
#         game_config.set_item_count(RangedWeapon, 10)
#         game_config.set_item_count(Food, 10)
#         game_config.set_item_count(Medicine, 10)
#         game_config.set_item_count(Animal, 10)
#         game_config.steps = 1000

#         def spawn_wild_animals(game):
#             for i in range(3):
#                 animal = DefaultItemFactory.create(WildAnimal)
#                 game.add_object(animal[0])
#                 GAME_LOGGER.add_event("SPAWNED", animal[0])

#         game_config.add_periodic_event(20, spawn_wild_animals, "Spawn Wild Animals")

#         return (GameMap(size, wrap=wrap), game_config)

#     # Create 6 AI Clones
#     tributes = []
#     for i in range(6):
#         # An AI is represented by a tuple, with the Class as the first element,
#         # and the name of the AI as the second
#         ai = (Ivan_AI, "AI" + str(i))
#         tributes.append(ai)

#     # Qualifier Rounds
#     # Uncomments to run more rounds, or modify the rounds list
#     # to include more rounds into the simulation
#     # (Note: More rounds = longer simulation!)
#     rounds = [
#         qualifer_map(4, False),
#         qualifer_map(4, False),
#         qualifer_map(4, False),
#         qualifer_map(4, True),
#         qualifer_map(4, True),
#         qualifer_map(4, True),
#     ]

#     match = Match(tributes, rounds)
#     print("Simulating matches... might take a while")

#     # Simulate without the graphics
#     match.text_simulate_all()

#     # Simulate a specific round with the graphics
#     # Due to limitation in the graphics framework,
#     # can only simulate one round at a time
#     # Round id starts from 0
#     # match.gui_simulate_round(0)
