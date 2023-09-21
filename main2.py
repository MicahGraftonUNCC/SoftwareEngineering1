import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    while True:

        # Asks user what size of sandwich they would like or if they would like to turn the system off or recieve a
        # report Cast to lower case, so it will work for any input caps or lower
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

        # if statement that is executed if the user choose a sandwich size
        if choice in ["small", "medium", "large"]:

            # the order_ingredients variable is set to the recipies dictionary for the selected size
            # and inputted with the ingredients dictionary
            order_ingredients = recipes[choice]["ingredients"]

            # cost variable is set to the recipies dictionary for the selected choice
            cost = recipes[choice]["cost"]

            # if statement that runs if there is enough resources to make the sandwich
            if sandwich_maker_instance.check_resources(order_ingredients):

                # coins variable is set equal to the output of the process_coins function
                coins = cashier_instance.process_coins()

                # if statement that runs if the transaction_result function returns true,
                # indicating that enough money was inserted
                if cashier_instance.transaction_result(coins, cost):
                    # the make_sandwich function is called with the choice by the user
                    # and the ingredients needed to make it
                    sandwich_maker_instance.make_sandwich(choice, order_ingredients)

                    # prints out that the sandwich is ready and gives a salutation
                    print(f"{choice} sandwich is ready. Bon Appétit!")

            # if there is not enough resources to make the sandwich
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
            for ingredient, quantity in sandwich_maker_instance.resources.items():
                # prints out the ingredient name and the current quantity of it to the user
                print(f"{ingredient}: {quantity}")


if __name__ == "__main__":
    main()


