class CoffeeMachine:
    def __init__(self):
        self.water = 900
        self.milk = 450
        self.coffee_beans = 160
        self.cups = 10
        self.money = 0

    def action(self):
        while True:
            action = input("What would you like to do? (buy, fill, take, report, exit): ").lower()
            if action == "buy":
                coffee_type = input("What kind of coffee would you like? (espresso, latte, cappuccino): ").lower()
                if coffee_type == "espresso":
                    if self.water < 50:
                        print("Sorry, not enough water!")
                    if self.coffee_beans < 20:
                        print("Sorry, not enough coffee beans!")
                    if self.cups < 1:
                        print("Sorry, not enough disposable cups!")
                    if self.water >= 50 and self.coffee_beans >= 20 and self.cups >= 1:
                        self.water -= 50
                        self.coffee_beans -= 20
                        self.cups -= 1
                        price_espresso = 5
                        pay_espresso = float(input(f"Please pay ${price_espresso}: "))
                        while pay_espresso != price_espresso:
                            if price_espresso > pay_espresso:
                                new_pay_espresso = float(input(f"Sorry, not enough ${price_espresso - pay_espresso} left: "))
                                pay_espresso += new_pay_espresso
                            if price_espresso < pay_espresso:
                                print(f"Here's your remaining ${pay_espresso - price_espresso}")
                                pay_espresso = price_espresso
                        else:
                            print("Here's your espresso! Enjoy!")
                            self.money += pay_espresso
                if coffee_type == "latte":
                    if self.water < 200:
                        print("Sorry, not enough water!")
                    if self.milk < 150:
                        print("Sorry, not enough milk!")
                    if self.coffee_beans < 30:
                        print("Sorry, not enough coffee beans!")
                    if self.cups < 1:
                        print("Sorry, not enough disposable cups!")
                    if self.water >= 200 and self.milk >= 150 and self.coffee_beans >= 30 and self.cups >= 1:
                        self.water -= 200
                        self.milk -= 150
                        self.coffee_beans -= 30
                        self.cups -= 1
                        price_latte = 10
                        pay_latte = float(input(f"Please pay ${price_latte}: "))
                        while pay_latte != price_latte:
                            if price_latte > pay_latte:
                                new_pay_latte = float(input(f"Sorry, not enough ${price_latte - pay_latte} left: "))
                                pay_latte += new_pay_latte
                            if price_latte < pay_latte:
                                print(f"Here's your remaining ${pay_latte - price_latte}")
                                pay_latte = price_latte
                        else:
                            print("Here's your latte! Enjoy!")
                            self.money += pay_latte
                if coffee_type == "cappuccino":
                    if self.water < 250:
                        print("Sorry, not enough water!")
                    if self.milk < 100:
                        print("Sorry, not enough milk!")
                    if self.coffee_beans < 30:
                        print("Sorry, not enough coffee beans!")
                    if self.cups < 1:
                        print("Sorry, not enough disposable cups!")
                    if self.water >= 250 and self.milk >= 100 and self.coffee_beans >= 30 and self.cups >= 1:
                        self.water -= 250
                        self.milk -= 100
                        self.coffee_beans -= 30
                        self.cups -= 1
                        price_cappuccino = 15
                        pay_cappuccino = float(input(f"Please pay ${price_cappuccino}: "))
                        while pay_cappuccino != price_cappuccino:
                            if price_cappuccino > pay_cappuccino:
                                new_pay_cappuccino = float(input(f"Sorry, not enough ${price_cappuccino - pay_cappuccino} left: "))
                                pay_cappuccino += new_pay_cappuccino
                            if price_cappuccino < pay_cappuccino:
                                print(f"Here's your remaining ${pay_cappuccino - price_cappuccino}")
                                pay_cappuccino = price_cappuccino
                        else:
                            print("Here's your cappuccino! Enjoy!")
                            self.money += pay_cappuccino
            elif action == "fill":
                fill_water = int(input("How much water would you like to add? "))
                self.water += fill_water
                fill_milk = int(input("How much milk would you like to add? "))
                self.milk += fill_milk
                fill_coffee_beans = int(input("How many coffee beans would you like to add? "))
                self.coffee_beans += fill_coffee_beans
                fill_cups = int(input("How many cups would you like to add? "))
                self.cups += fill_cups
            elif action == "take":
                print(f"I took ${self.money} from the coffee machine.")
                self.money -= self.money
            elif action == "report":
                print(
                    f"Water = {self.water} \nMilk = {self.milk} \nCoffee Beans = {self.coffee_beans} \nCups = {self.cups} \nMoney = {self.money}")
            elif action == "exit":
                break


coffee_machine = CoffeeMachine()
coffee_machine.action()