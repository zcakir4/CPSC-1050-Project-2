'''

Author:         Beyza Cakir
Date:           05/02/24
Assignment:     RPG 
Course:         CPSC1050
Lab Section:    001


CODE DESCRIPTION: 
Culinary Chaos is role play game where the player can choose a cooking role and navigate the chaotic world of cooking. The goal is for the player to maximize the kitchen's success rate.

'''

import random
import os


class Chef:
    # This class represents a chef role in the game
    def __init__(self, name, skill_level):
        # Initializes chef object with name and skill level
        self.name = name
        self.skill_level = skill_level

        self.inventory = {
                "Flour": 50,
                "Eggs": 30,
                "Milk": 20,
                "Vegetables": 40,
                "Meat": 25
            }

        def prepare_ingredients(self):
            # Player is preparing the ingredients for the dish
            print(f'{self.name} is preparing the ingredients.')
            self.update_inventory()

        def update_inventory(self):
            # Update the inventory based on the ingredients used
            ingredients_used = {
                "Flour": 2,
                "Eggs": 3,
                "Milk": 1,
                "Vegetables": 5,
                "Meat": 1
            }

            for item, quantity in ingredients_used.items():
                if self.inventory[item] >= quantity:
                    self.inventory[item] -= quantity
                    print(f"Used {quantity} {item} from the inventory.")
                else:
                    print(f"Not enough {item} in the inventory. Unable to prepare the dish.")
                    return

            print("All ingredients have been prepared.")


    def cook_dish(self, dish):
        # Player is cooking a dish of their choice
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
        # Player is putting the prepared food on a plate
        print(f'{self.name} is plating cuisine.')


class SousChef(Chef):
    # This class represents a SousChef role in the game
    def __init__(self, name, skill_level):
        super().__init__(name, skill_level)
        self.inventory = {
            "Flour": 50,
            "Eggs": 30,
            "Milk": 20,
            "Vegetables": 40,
            "Meat": 25
        }

    def assist_chef(self, chef):
        # Player gets help from another player
        print(f'{self.name} is assisting Gordon Ramsey.')

    def manage_inventory(self):
        # Player is managing the kitchen inventory
        print(f'{self.name} is managing the kitchen inventory.')
        low_inventory = [item for item, quantity in self.inventory.items() if quantity < 10]
        if low_inventory:
            print("The following inventory items are running low:")
            for item in low_inventory:
                print(f"- {item}")
            print("Restocking the inventory...")
            self.restock_inventory()
        else:
            print("The kitchen inventory is in good shape.")


    def coordinate_team(self, team):
        # Player forms the team
        print(f'{self.name} is coordinating the team.')

class Expediter(Chef):
    def __init__(self, name, skill_level):
        super().__init__(name, skill_level)

    def prioritize_orders(self, orders):
        # Player is prioritizing orders
        print(f'{self.name} is prioritizing the orders by making sure the other chefs are cooking.')

    def monitor_progress(self, team):
        # Player monitors the team progress
        print(f'{self.name} is monitoring the team\'s progress.')
        print(f'Progress level is at 100%')
        

    def communicate_status(self, team):
        # Player communicates the status to the team
        print(f'{self.name} is communicating the team\'s status.')
        print('Gordon Ramsey and his minion chefs report that the kitchen is on a 100% success rate')


class Dishwasher(Chef):
    def __init__(self, name, skill_level):
        super().__init__(name, skill_level)
        self.inventory = {
            "Flour": 50,
            "Eggs": 30,
            "Milk": 20,
            "Vegetables": 40,
            "Meat": 25
        }

    def clean_dishes(self):
        # Player is cleaning dishes
        print(f'{self.name} is cleaning the dishes.')
        

    def restock_supplies(self):
        # Player isrestocking kitchen supplies
        print(f'{self.name} is restocking the kitchen supplies')
        for item, quantity in self.inventory.items():
            if quantity < 50:
                self.inventory[item] = 50
                print(f"Restocked {item} to 50.")



    def support_team(self, team):
        # Player is supporting the team
        print(f'{self.name} is supporting the team')

# Game Functions
def create_map():
    # A custom kitchen map is made
    print('Creating a custom kitchen map.')

def save_game(team, kitchen_state):
    # The game is being saved the game state
    print(f'Saving the game state')

def load_game():
    # The game is loading a saved game
    print('Loading a saved game')

def output_log(team_performance):
    # An output log is being generated
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
        print(f'   5. Assist Chef')
        print(f'   6. Prioritize Orders')
        print(f'   7. Monitor Progress')
        print(f'   8. Communicate Status')
        print(f'   9. Clean Dishes')
        print(f'   10. Restock Supplies')
        print(f'   11. Support Team')
        print(f'   12. Save Game')
        print(f'   13. Load Game')
        print(f'   14. Exit')


        # Handles user input
        try:
            choice = int(input('Enter your choice (1-14):\n'))
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
                if isinstance(player, SousChef):
                    player.assist_chef(player)
                else:
                    print('Only the SousChef can assist the Chef.')
            elif choice == 6:
                if isinstance(player, Expediter):
                    player.prioritize_orders(['Order1', 'Order2', 'Order3'])
                else:
                    print('Only the Expediter can prioritize orders.')
            elif choice == 7:
                if isinstance(player, Expediter):
                    player.monitor_progress(['Player1', 'Player2', 'Player3'])
                else:
                    print('Only the Expediter can monitor the team\'s progress.')
            elif choice == 8:
                if isinstance(player, Expediter):
                    player.communicate_status(['Player1', 'Player2', 'Player3'])
                else:
                    print('Only the Expediter can communicate the team\'s status.')
            elif choice == 9:
                if isinstance(player, Dishwasher):
                    player.clean_dishes()
                else:
                    print('Only the Dishwasher can clean the dishes.')
            elif choice == 10:
                if isinstance(player, Dishwasher):
                    player.restock_supplies()
                else:
                    print('Only the Dishwasher can restock the kitchen supplies.')
            elif choice == 11:
                if isinstance(player, Dishwasher):
                    player.support_team(['Player1', 'Player2', 'Player3'])
                else:
                    print('Only the Dishwasher can support the team.')
            elif choice == 12:
                save_game([player], 'kitchen_state')
            elif choice == 13:
                load_game()
            elif choice == 14:
                print('Exiting the game.')
                break
            else:
                print('Invalid choice. Please try again.')
        except ValueError:
            print('Invalid input. Please enter a number.')



if __name__ == "__main__":
     main()




    