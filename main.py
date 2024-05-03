'''

Author:         Beyza Cakir
Date:           05/02/24
Assignment:     RPG
Course:         CPSC1050
Lab Section:    001


CODE DESCRIPTION:
Culinary Chaos is role play game where the player switches between Chef and SousChef navigate the chaotic world of cooking. The goal is for the player to maximize the kitchen's success rate.

'''

import random
import os

class Inventory:
    def __init__(self):
        # Player has full inventory -- 50 of each ingredient
        self.items = {
            "Flour": 50,
            "Eggs": 30,
            "Milk": 20,
            "Vegetables": 40,
            "Meat": 25
        }
        # Player has 0 dishes ready to cook initially
        self.dishesReadyToCook = {
            "Spaghetti Bolognese": 0,
            "Chicken Curry": 0,
            "Vegetable Stir-Fry": 0,
            "Beef Lasagna": 0,
            "Grilled Salmon": 0
        }
        # Player has 0 dishes ready to serve initially
        self.dishesReadyToServe = {
            "Spaghetti Bolognese": 0,
            "Chicken Curry": 0,
            "Vegetable Stir-Fry": 0,
            "Beef Lasagna": 0,
            "Grilled Salmon": 0
        }
        # Player has 5 clean plates initially
        self.clean_dishes = 5

    def update(self, ingredients_used):
        for item, quantity in ingredients_used.items():
            if self.items[item] >= quantity:
                self.items[item] -= quantity
            else:
                print(f"Not enough {item} in the inventory. Unable to prepare the dish.")

    def restock(self, item, quantity):
        self.items[item] = quantity

    def check_availability(self, ingredients_needed):
        for item, quantity in ingredients_needed.items():
            if self.items[item] < quantity:
                return False
        return True

    def get_string_representation(self):
        return str(self.items)

class Dish:
    def __init__(self, name, ingredients_needed, minimum_skill_level):
        # Initializes dish object with name and skill level
        self.name = name
        self.ingredients_needed = ingredients_needed
        self.minimum_skill_level = minimum_skill_level

    def checkIfPlayerCanCook(self, player):
        # Checks if the player can cook the dish
        if player.skill_level >= self.minimum_skill_level:
            return True
        else:
            print(f"{player.name} does not have the required skill level to cook this dish.")
            return False

class BaseCook:
    def __init__(self, name, skill_level):
        self.name = name
        self.inventory = Inventory()
        self.skill_level = skill_level

    def prepare_ingredients(self, dishes):
        # Select a Dish
        print("\nAvailable dishes:")
        for i, dish in enumerate(dishes, start=1):
            print(f"{i}. {dish.name}")
        print()

        dish = None
        while True:
            user_choice = int(input("What dish would you like to prepare the ingredients for out of the list?\n"))
            if user_choice < 1 or user_choice > 5:
                print("Sorry, that dish is not on the list. Please choose from the available dishes:")
                for dish in dishes:
                    print("- " + dish)
            else:
                dish = dishes[user_choice - 1]
                print(f"Great, you've chosen to prepare the ingredients for {dish.name}!")
                break

        # Player is preparing the ingredients for the dish
        print(f'{self.name} is preparing the ingredients.')

        if self.inventory.check_availability(dish.ingredients_needed):
            self.inventory.update(dish.ingredients_needed)
            self.inventory.dishesReadyToCook[dish.name] += 1
            print("All ingredients have been prepared.")
        else:
            print("Not enough ingredients in the inventory. Unable to prepare the dish.")

    def cook_dish(self, dishes):
        # Player is cooking a dish of their choice
        print("\nAvailable dishes:")
        for i, dish in enumerate(dishes, start=1):
            print(f"{i}. {dish.name}")
        print()

        while True:
            user_choice = int(input("What dish would you like to cook out of the list?\n"))
            if user_choice < 1 or user_choice > 5:
                print("Sorry, that dish is not on the list. Please choose from the available dishes:")
                for dish in dishes:
                    print("- " + dish)
            elif dishes[user_choice - 1].checkIfPlayerCanCook(self) == True and self.inventory.dishesReadyToCook[dishes[user_choice - 1].name] > 0:
                print(f"Great, you've chosen to cook {dishes[user_choice - 1].name}!")
                print(f"{self.name} is cooking {dishes[user_choice - 1].name}.")
                self.inventory.dishesReadyToCook[dishes[user_choice - 1].name] -= 1
                self.inventory.dishesReadyToServe[dishes[user_choice - 1].name] += 1
                break
            else:
                print("Sorry, you can't cook this dish because you lack the skill or prepared ingredients.")
                break

class Chef(BaseCook):
    # This class represents a chef role in the game
    def __init__(self, name):
        # Chef has skill level of 5/5
        super().__init__(name, 5)

    # Only the Chef can serve a dish
    def serve_dish(self, dishes):
        # Select a Dish
        print("\nAvailable dishes:")
        for i, dish in enumerate(dishes, start=1):
            print(f"{i}. {dish.name}")
        print()

        dish = None
        while True:
            user_choice = int(input("What dish would you like to serve out of the list?\n"))
            if user_choice < 1 or user_choice > 5:
                print("Sorry, that dish is not on the list. Please choose from the available dishes:")
                for dish in dishes:
                    print("- " + dish)
            else:
                dish = dishes[user_choice - 1]
                break

        if self.inventory.dishesReadyToServe[dish.name] > 0:
            if self.inventory.clean_dishes == 0:
                print("There are no clean plates. Unable to serve the dish.")
            else:
                print(f"{self.name} is serving {dish.name}.")
                self.inventory.dishesReadyToServe[dish.name] -= 1
                self.inventory.clean_dishes -= 1
        else:
            print(f"{self.name} does not have any {dish.name} to serve.")

class SousChef(BaseCook):
    # This class represents a chef role in the game
    def __init__(self, name):
        # SousChef has a skill level of 3/5
        super().__init__(name, 3)

    # Only the SousChef can clean plates
    def cleanPlate(self):
        if self.inventory.clean_dishes > 0:
            print(f"{self.name} is cleaning a plate.")
            self.inventory.clean_dishes += 1
        else:
            print("There are no dirty plates to clean.")

# Game Functions
def output_log(player):
    # An output log is being generated
    print('Generating an ouput log')

def switch_character(chef, sousChef):
    print('Which character would you like to switch to:')
    print('   1. Chef')
    print('   2. SousChef')

    current_player_character = 0
    while True:
        try:
            choice = int(input(f'Enter your choice (1-2):\n'))
            if 1 <= choice <= 2:
                current_player_character = choice
                break
            else:
                print(f'Invalid choice. Please try again.')
        except ValueError:
            print(f'Invalid input. Please enter a number')

    if current_player_character == 1:
        print(f'You are a Chef now!\n')
        return chef
    elif current_player_character == 2:
        print(f'You are a SousChef now!\n')
        return sousChef

def main():
    dishes = [
        Dish("Spaghetti Bolognese", {"Flour": 2, "Eggs": 3, "Milk": 1, "Vegetables": 3, "Meat": 3}, 4),
        Dish("Chicken Curry", {"Flour": 0, "Eggs": 3, "Milk": 1, "Vegetables": 5, "Meat": 1}, 2),
        Dish("Vegetable Stir-Fry", {"Flour": 2, "Eggs": 3, "Milk": 1, "Vegetables": 5, "Meat": 0}, 4),
        Dish("Beef Lasagna", {"Flour": 5, "Eggs": 1, "Milk": 0, "Vegetables": 5, "Meat": 4}, 5),
        Dish("Grilled Salmon", {"Flour": 2, "Eggs": 3, "Milk": 1, "Vegetables": 5, "Meat": 1}, 2)
    ]

    print(f'Welcome to Culinary Chaos')
    name = input("Enter your Chef's name: ").capitalize()
    chef = Chef(name)
    name = input("Enter your SousChef's name: ").capitalize()
    sous_chef = SousChef(name)

    # Pick current player
    player = switch_character(chef, sous_chef)

    while True:
        # Displays game menu
        print('Game Menu: ')
        print('What would you like to do today:')
        print(f'   1. Prepare Ingredients')
        print(f'   2. Cook a Dish')
        print(f'   3. Serve a Dish')
        print(f'   4. Clean Dishes')
        print(f'   5. Output Game Log')
        print(f'   6. Switch Player')
        print(f'   7. Exit')

        try:
            choice = int(input('Enter your choice (1-8):\n'))
            if choice == 1:
                player.prepare_ingredients(dishes)
            elif choice == 2:
                player.cook_dish(dishes)
            elif choice == 3:
                if isinstance(player, Chef):
                    player.serve_dish(dishes)
                else:
                    print('Only the Chef can serve a dish.')
            elif choice == 4:
                if isinstance(player, SousChef):
                    player.cleanPlate(self)
                else:
                    print('Only the SousChef can clean dishes.')
            elif choice == 5:
                output_log(player)
            elif choice == 6:
                # switch player
                player = switch_character(chef, sous_chef)
            elif choice == 7:
                print('Exiting the game.')
                break
            else:
                print('Invalid choice. Please try again.')
        except ValueError:
            print('Invalid input. Please enter a number.')

if __name__ == "__main__":
     main()