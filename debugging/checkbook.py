class Checkbook:
    """
    A simple checkbook class for managing deposits, withdrawals, and balance checks.
    """

    def __init__(self):
        """
        Initializes the Checkbook with a balance of $0.00.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Adds the specified amount to the current balance.

        Parameters:
        amount (float): The amount to deposit. Must be greater than zero.

        Returns:
        None
        """
        if amount <= 0:
            print("Error: Deposit amount must be greater than zero.")
        else:
            self.balance += amount
            print("Deposited ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Subtracts the specified amount from the current balance if sufficient funds exist.

        Parameters:
        amount (float): The amount to withdraw. Must be greater than zero and not exceed the current balance.

        Returns:
        None
        """
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance.

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to interact with the Checkbook. Provides options to deposit, withdraw, check balance, or exit.

    Returns:
    None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            print("Thank you for using the Checkbook. Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Error: Please enter a valid numeric amount.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Error: Please enter a valid numeric amount.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
