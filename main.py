### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    # Takes in machine_resources as a attribute and assigns the input to the self variable
    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    # Takes ingredients as a attribute and returns true if the order can be made and false if ingredients are
    # insufficient
    # adding commit
    def check_resources(self, ingredients):
        for ingredient, quantity in ingredients.items():
            if self.machine_resources.get(ingredient) is None or self.machine_resources[ingredient] < quantity:
                return False
        return True

    # Takes coins inserted and returns the total of them
    #commit 2
    def process_coins(self):
        coins = {"large dollar": 1, "half dollar": .5, "quarter": .25, "nickel": .05}
        total = 0
        print(f"Please insert coins.")
        for coin in coins:
            try:
                amount = int(input(f"How many {coin}s?: "))
                total += amount * coins[coin]
            except ValueError:
                pass
        return total

    # Takes coins and cost as attributes, and returns users change if there is enough money
    # and returns all money if it is not enough
    def transaction_result(self, coins, cost):
        if coins < cost:
            print(f"Sorry that's not enough money. Money refunded.")
            return False
        else:
            change = coins - cost
            if change > 0:
                print(f"Here is ${change} in change.")
            return True

    # Takes sandwhich_size and order_ingredients as attributes
    # and subtracts the resources used from the resources dictionary
    # has no return type
    def make_sandwich(self, sandwich_size, order_ingredients):
        for ingredient, quantity in order_ingredients.items():
            self.machine_resources[ingredient] -= quantity


### Make an instance of SandwichMachine class and write the rest of the codes ###
SandwichMachine = SandwichMachine(resources)

# While the system has not been turned off
while True:

    # Asks user what size of sandwhich they would like or if they would like to turn the system off or recieve a report
    # Casted to lower case so it will work for any input caps or lower
    choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

    # if statement that is executed if the user choose a sandwich size
    if choice in ["small", "medium", "large"]:

        # the order_ingredients variable is set to the recipies dictionary for the selected size
        # and inputted with the ingredients dictionary
        order_ingredients = recipes[choice]["ingredients"]

        # cost variable is set to the recipies dictionary for the selected choice
        cost = recipes[choice]["cost"]

        # if statement that runs if there is enough resources to make the sandwich
        if SandwichMachine.check_resources(order_ingredients):

            # coins variable is set equal to the output of the process_coins function
            coins = SandwichMachine.process_coins()

            # if statement that runs if the transaction_result function returns true,
            # indicating that enough money was inserted
            if SandwichMachine.transaction_result(coins, cost):

                # the make_sandwhich function is called with the choice by the user
                # and the ingredients needed to make it
                SandwichMachine.make_sandwich(choice, order_ingredients)

                # prints out that the sandwich is ready and gives a salutation
                print(f"{choice} sandwich is ready. Bon Appétit!")

        # if there is not enough resources to make the sandwhich
        else:

            # prints out a apology to the user and informs them we are out of resources
            print("We are out of the required ingredients, sorry.")

    # else if the user chose the off option then the system breaks and ends
    elif choice == "off":
        break

    # else if the user cose report
    elif choice == "report":

        # a for loop that goes through each ingredient in the dictionary
        # and goes through the quantity given by the machine_resources function
        for ingredient, quantity in SandwichMachine.machine_resources.items():

            # prints out the ingredient name and the current quantity of it to the user
            print(f"{ingredient}: {quantity}")
