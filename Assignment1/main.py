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

class SandwichMaker:
    def __init__(self):
        # Resources initialized
        self.resources = {
            "bread": 12,  # slices
            "ham": 18,  # slices
            "cheese": 24  # ounces
        }

        self.recipes = {
            "small": {
                "ingredients": {"bread": 2, "ham": 4, "cheese": 4},
                "cost": 1.75
            },
            "medium": {
                "ingredients": {"bread": 4, "ham": 6, "cheese": 8},
                "cost": 3.25
            },
            "large": {
                "ingredients": {"bread": 6, "ham": 8, "cheese": 12},
                "cost": 5.50
            }
        }

    def check_resources(self, sandwich_size):
        """Check if there are enough resources to make the sandwich."""
        ingredients = self.recipes[sandwich_size]["ingredients"]
        for item in ingredients:
            if self.resources[item] < ingredients[item]:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Calculate the total value of the inserted coins."""
        print("Please insert coins.")
        large_dollars = int(input("How many large dollars?: "))
        half_dollars = int(input("How many half dollars?: "))
        quarters = int(input("How many quarters?: "))
        nickels = int(input("How many nickels?: "))

        total = (large_dollars * 1.00) + (half_dollars * 0.50) + (quarters * 0.25) + (nickels * 0.05)
        return total

    def transaction_result(self, sandwich_size, money_inserted):
        """Check if the user inserted enough money for the sandwich."""
        cost = self.recipes[sandwich_size]["cost"]
        if money_inserted >= cost:
            change = round(money_inserted - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size):
        """Deduct resources and make the sandwich."""
        ingredients = self.recipes[sandwich_size]["ingredients"]
        for item in ingredients:
            self.resources[item] -= ingredients[item]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

    def report(self):
        """Show the current status of resources."""
        for item, amount in self.resources.items():
            print(f"{item.capitalize()}: {amount}")

    def run(self):
        """Main logic for running the sandwich maker."""
        while True:
            choice = input("What would you like? (small/medium/large/off/report): ").lower()

            if choice == "off":
                break
            elif choice == "report":
                self.report()
            elif choice in self.recipes:
                if self.check_resources(choice):
                    money_inserted = self.process_coins()
                    if self.transaction_result(choice, money_inserted):
                        self.make_sandwich(choice)
            else:
                print("Invalid option.")


# Instantiate the sandwich maker and run it
if __name__ == "__main__":
    sandwich_maker = SandwichMaker()
    sandwich_maker.run()
