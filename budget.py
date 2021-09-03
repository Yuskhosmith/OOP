"""Budget App
Create a Budget class that can instantiate objects based on different budget categories like
food, clothing, and entertainment. These objects should allow for
1. Depositing funds to each of the categories
2. Withdrawing funds from each category
3. Computing category balances
4. Transferring balance amounts between categories
Push your code to GitHub, and submit the repo link.
"""


class Budget():
    def __init__(self, fund):
        self.fund = fund
        self.category = ["Food", "Clothing", "Entertainment"]
        self.food_fund = 0
        self.clothing_fund = 0
        self.entertainment_fund = 0

    def options(self):
        user_operation = int(input("What would you like to do \n1) Deposit fund to a category\n2) Withdraw Fund from "
                                   "a category\n3) Balances\n4) Transfer fund between "
                                   "categories\n==================================>>\n"
                                   "---------------------------------->>\n"))
        if user_operation == 1:
            self.deposit()

        elif user_operation == 2:
            self.withdrawal()

        elif user_operation == 3:
            self.compute_balances()

        elif user_operation == 4:
            self.transfer_fund()

        else:
            print("Input one of the options")
            self.options()

    def deposit(self):

        deposit_category = int(input("Where would you like to deposit to \n1) Food\n2) Clothing\n3) Entertainment\n"))

        if deposit_category == 1:
            food_fund = int(input("How much would you like to deposit\n"))
            self.fund -= food_fund
            self.food_fund += food_fund
            self.options()

        elif deposit_category == 2:
            clothing_fund = int(input("How much would you like to deposit\n"))
            self.fund -= clothing_fund
            self.clothing_fund += clothing_fund
            self.options()

        elif deposit_category == 3:
            entertainment_fund = int(input("How much would you like to deposit\n"))
            self.fund -= entertainment_fund
            self.entertainment_fund += entertainment_fund
            self.options()
        else:
            print("Input one of the options")
            self.deposit()

    def withdrawal(self):
        withdrawal_category = int(input("Where would you like to withdraw from \n1) Food\n2) Clothing\n3) "
                                        "Entertainment\n"))
        if withdrawal_category == 1:
            amount_to_withdraw = int(input("How much would you like to withdraw\n"))
            if self.bal_check(amount_to_withdraw, self.food_fund):
                print("Successful")
                self.options()
        elif withdrawal_category == 2:
            amount_to_withdraw = int(input("How much would you like to withdraw\n"))
            if self.bal_check(amount_to_withdraw, self.clothing_fund):
                print("Successful")
                self.options()
        elif withdrawal_category == 3:
            amount_to_withdraw = int(input("How much would you like to withdraw\n"))
            if self.bal_check(amount_to_withdraw, self.entertainment_fund):
                print("Successful")
                self.options()
        else:
            print("Input one of the options")
            self.withdrawal()

    def transfer_destination_question(self):
        response = int(input("Where will you like to transfer to\n1) Food\n2)Clothing \n3)Entertainment \n4)Exit"))
        return response

    def transfer_fund(self):
        response = int(input("From where do you want to transfer \n1) Food\n2)Clothing \n3)Entertainment \n4)Exit"))
        if response == 1:
            location_response = self.transfer_destination_question()
            if location_response == 1:

        elif response == 2:
            pass
        elif response == 3:
            pass
        elif response == 4:
            pass
        else:
            print("Invalid response")
            self.transfer_fund()

    def bal_check(self, amount_to_withdraw, amount_available):
        if amount_to_withdraw > amount_available:
            print("You have can't withdraw more than you have")
            self.options()
        else:
            return True

    def compute_balances(self):
        print(f"Food Fund : {self.food_fund}\nClothing fund : {self.clothing_fund}\nEntertainment fund : "
              f"{self.entertainment_fund}\n=========\nTotal fund : {self.fund}")


budget = Budget(1000)
budget.options()
