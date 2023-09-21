class Cashier:
    def __init__(self):
        pass

    # Takes coins inserted and returns the total of them
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
