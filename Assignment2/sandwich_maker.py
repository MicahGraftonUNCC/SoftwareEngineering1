class SandwichMaker:

    def __init__(self, resources):
        self.resources = resources

    # Takes ingredients as a attribute and returns true if the order can be made and false if ingredients are
    # insufficient
    def check_resources(self, ingredients):
        for ingredient, quantity in ingredients.items():
            if self.resources.get(ingredient) is None or self.resources[ingredient] < quantity:
                return False
        return True

    # Takes sandwich_size and order_ingredients as attributes
    # and subtracts the resources used from the resources dictionary
    # has no return type
    def make_sandwich(self, sandwich_size, order_ingredients):
        for ingredient, quantity in order_ingredients.items():
            self.resources[ingredient] -= quantity
