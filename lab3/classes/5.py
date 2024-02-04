class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        else:
            print("Insufficient funds. Withdrawal not allowed.")

# Example of using the class:
account = Account(owner="John Doe", balance=1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(1200)  # Attempt to overdraw
account.deposit(300)

'''Определен класс Account с атрибутами owner (владелец) и balance (баланс) и двумя методами deposit (внесение) и withdraw (снятие). 
Снятия не могут превышать доступный баланс. Создан экземпляр класса, выполнены несколько внесений и снятий,
и проведено тестирование, чтобы убедиться, что счет не может быть перерасходован.

1. Класс Account:
   - Метод __init__ является конструктором класса и инициализирует объект с заданными атрибутами owner и balance (по умолчанию 0).
   - Метод deposit позволяет вносить деньги на счет, проверяя, что сумма положительна.
   - Метод withdraw позволяет снимать деньги с учетом ограничения доступного баланса.

Пример использования класса:
account = Account(owner="John Doe", balance=1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(1200)  # Попытка превысить баланс
account.deposit(300)'''