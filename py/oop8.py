class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # public attribute
        self._balance = balance  # protected attribute
        self.__pin = 1234  # private attribute

    def deposit(self, amount):
        self._balance += amount  # επιτρέπεται η πρόσβαση σε protected μέλος
        print(f"Κατεβλήθη ποσό {amount}. Νέο υπόλοιπο: {self._balance}")

    def __verify_pin(self, pin):  # private μέθοδος
        return pin == self.__pin

    def withdraw(self, amount, pin):
        if self.__verify_pin(pin):
            if amount <= self._balance:
                self._balance -= amount
                print(f"Αναλήφθηκε ποσό {amount}. Υπόλοιπο: {self._balance}")
            else:
                print("Μη επαρκές υπόλοιπο.")
        else:
            print("Λανθασμένος PIN!")


account = BankAccount("Christos", 1000)

print(account.owner)  # Public: επιτρέπεται
# print(account._balance)  # Protected: τεχνικά επιτρέπεται αλλά ΔΕΝ συνιστάται
# print(account.__pin)     # Private: προκαλεί σφάλμα AttributeError

account.deposit(200)
account.withdraw(100, 1234)

# Μπορούμε (αν και δεν πρέπει) να προσπελάσουμε το private όνομα με name mangling:
print(account._BankAccount__pin)  # Δυνατό, αλλά αντίθετο με τη σύμβαση
