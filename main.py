'''

Author:         Beyza Cakir
Date:           05/02/24
Assignment:     RPG 
Course:         CPSC1050
Lab Section:    001


CODE DESCRIPTION: The game, Culinary Chaos is role play game where the player can choose a role in 
the cooking world.

'''


import random
import os


class Chef:
    def __init__(self, name, skill_level):
        self.name = name
        self.skill_level = skill_level

    def prepare_ingredients(self):
        # Ingredients are being prepared
        print(f'{self.name} is preparing the ingredients.')


    def cook_dish(self, dish):
        # User is cooking a dish of their choice
        dishes = ["Spaghetti Bolognese", "Chicken Curry", "Vegetable Stir-Fry", "Beef Lasagna", "Grilled Salmon"]
        print("\nAvailable dishes:")
        for i, dish in enumerate(dishes, start=1):
            print(f"{i}. {dish}")
        print()

        while True:
            user_choice = int(input("What dish would you like to cook out of the list?\n"))
            if user_choice < 1 or user_choice > 5:
                print("Sorry, that dish is not on the list. Please choose from the available dishes:")
                for dish in dishes:
                    print("- " + dish)
            else:
                print(f"Great, you've chosen to cook {dishes[user_choice - 1]}!")
                print(f"{self.name} is cooking {dishes[user_choice - 1]}.")
                break
                    

    def plate_dish(self, dish):
        # User is putting the prepared food on a plate
        print(f'{self.name} is plating {dish}.')

class SousChef(Chef):
    def __init__(self, name, skill_level):
        super().__init__(name, skill_level)

    def assist_chef(self, chef):
        # User gets help from another player
        print(f'{self.name} is assisting {chef.name}.')

    def manage_inventory(self):
        # User is managing the kitchen inventory
        print(f'{self.name} is managing the kitchen inventory.')

    def coordinate_team(self, team):
        # User forms the team
        print(f'{self.name} is coordinating the team.')

class Expediter(Chef):
    def __init__(self, name, skill_level):
        super().__init__(name, skill_level)

    def prioritize_orders(self, orders):
        # User is prioritizing orders
        print(f'{self.name} is prioritizing the orders.')

    def monitor_progress(self, team):
        # User monitors the team progress
        print(f'{self.name} is monitoring the team\'s progress.')
        

    def communicate_status(self, team):
        # User communicates the status to the team
        print(f'{self.name} is communicating the team\'s status.')

class Dishwasher(Chef):
    def __init__(self, name, skill_level):
        super().__init__(name, skill_level)

    def clean_dishes(self):
        # User is cleaning dishes
        print(f'{self.name} is cleaning the dishes.')

    def restock_supplies(self):
        # User isrestocking kitchen supplies
        print(f'{self.name} is restocking the kitchen supplies')

    def support_team(self, team):
        # User is supporting the team
        print(f'{self.name} is supporting the team')

# Game Functions
def create_map():
    # Logic for creating a custom kitchen map
    print('Creating a custom kitchen map.')

def save_game(team, kitchen_state):
    # Logic for saving the game state
    print(f'Saving the game state')

def load_game():
    # Logic for loading a saved game
    print('Loading a saved game')

def output_log(team_performance):
    # Logic for generating an output log
    print('Generating an ouput log')

def select_character():
    print('Choose your character:')
    print('   1. Chef')
    print('   2. SousChef')
    print('   3. Expediter')
    print('   4. Dishwasher')


    while True:
        try:
            choice = int(input(f'Enter your choice (1-4):\n'))
            if 1 <= choice <= 4:
                return choice
            else:
                print(f'Invalid choice. Please try again.')
        except ValueError:
            print(f'Invalid input. Please enter a number')



def main():
    print(f'Welcome to Culinary Chaos')
    name = input("Enter your name: ").capitalize()
    # The choice of the player's character is chosen
    player_character = select_character()

    # Player's role is based on the user's choice
    if player_character == 1:
        player = Chef(name, 5)
        print(f'You are a Chef!\n')
    elif player_character == 2:
        player = SousChef(name, 5)
        print(f'You are a SousChef!\n')
    elif player_character == 3:
        player = Expediter(name, 5)
        print(f'You are an Expediter!\n')
    else:
        player = Dishwasher(name, 5)
        print(f'You are a Dishwasher!\n')


    
    while True:
        # Displays game menu
        print('Game Menu: ')
        print('What would you like to do today:')
        print(f'   1. Prepare Ingredients')
        print(f'   2. Cook a Dish')
        print(f'   3. Plate a Dish')
        print(f'   4. Manage Inventory')
        print(f'   5. Save Game')
        print(f'   6. Load Game')
        print(f'   7. Exit')

        # Handles user input
        try:
            choice = int(input('Enter your choice (1-7):\n'))
            if choice == 1:
                player.prepare_ingredients()
            elif choice == 2:
                player.cook_dish('Dish')
            elif choice == 3:
                player.plate_dish('Dish')
            elif choice == 4:
                if isinstance(player, SousChef):
                    player.manage_inventory()
                else:
                    print('Only the SousChef can manage the inventory.')
            elif choice == 5:
                save_game([player], 'kitchen_state')
            elif choice == 6:
                load_game()
            elif choice == 7:
                print('Exiting the game.')
                break
            else:
                print('Invalid choice. Please try again.')
        except ValueError:
            print('Invalid input. Please enter a number.')

        # Update game state
        # Render game world



if __name__ == "__main__":
     main()




    