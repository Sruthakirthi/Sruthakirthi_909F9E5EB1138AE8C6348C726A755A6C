
class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = initial_balance

    def deposit(self, amount_inr):
        if amount_inr > 0:
            self.balance += amount_inr
            return f"Deposited ₹{amount_inr}. New balance: ₹{self.balance}"
        else:
            return "Invalid deposit amount. Please enter a positive amount in ₹."

    def withdraw(self, amount_inr):
        if amount_inr > 0 and amount_inr <= self.balance:
            self.balance -= amount_inr
            return f"Withdrew ₹{amount_inr}. New balance: ₹{self.balance}"
        elif amount_inr > self.balance:
            return "Insufficient funds. Withdrawal failed."
        else:
            return "Invalid withdrawal amount. Please enter a positive amount in ₹."

    def display_balance(self):
        return f"Account balance for {self.account_holder_name}: ₹{self.balance}"


# Example usage:
class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = initial_balance

    def deposit(self, amount_inr):
        if amount_inr > 0:
            self.balance += amount_inr
            return f"Deposited ₹{amount_inr}. New balance: ₹{self.balance}"
        else:
            return "Invalid deposit amount. Please enter a positive amount in ₹."

    def withdraw(self, amount_inr):
        if amount_inr > 0 and amount_inr <= self.balance:
            self.balance -= amount_inr
            return f"Withdrew ₹{amount_inr}. New balance: ₹{self.balance}"
        elif amount_inr > self.balance:
            return "Insufficient funds. Withdrawal failed."
        else:
            return "Invalid withdrawal amount. Please enter a positive amount in ₹."

    def display_balance(self):
        return f"Account balance for {self.account_holder_name}: ₹{self.balance}"


# Example usage:
if __name__ == "__main__":
    account = BankAccount("123456", "Karthik", 10000)

    print(account.display_balance())
    print(account.deposit(500))
    print(account.withdraw(200))
    print(account.display_balance())
    print(account.withdraw(2000))