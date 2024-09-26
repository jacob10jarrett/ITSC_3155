class SandwichMaker:
    def __init__(self, resources):
        self.resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources."""
        for item in order_ingredients:
            self.resources[item] -= order_ingredients[item]
        print(f"Here is your {sandwich_size} sandwich. Enjoy!")
