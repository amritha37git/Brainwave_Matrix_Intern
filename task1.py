class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def authenticate(self, pin):
        return pin == self.pin

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn. Remaining balance: ₹{self.balance}")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")

def main():
    atm = ATM(pin="1234", balance=5000)

    pin = input("Enter your PIN: ")
    if not atm.authenticate(pin):
        print("Invalid PIN!")
        return

    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            atm.deposit(amount)
        elif choice == "3":
            amount = int(input("Enter withdrawal amount: "))
            atm.withdraw(amount)
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
