class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        quarters = int(input("how many quarters?: ")) * 0.25
        dimes = int(input("how many dimes?: ")) * 0.10
        nickels = int(input("how many nickels?: ")) * 0.05
        pennies = int(input("how many pennies?: ")) * 0.01
        total = quarters + dimes + nickels + pennies
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False
