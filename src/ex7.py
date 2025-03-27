# Write a Python program to create a class representing a bank. 
# Include methods for managing customer accounts and transactions.

class Customer:
    def __init__(self, name, balance=0.0):
        self.__name = name
        self.__balance = balance

    @property 
    def name(self):
        return self.__name
    
    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            raise Exception('Insufficient funds')
        self.__balance -= amount
        return self.__balance

    def __str__(self):
        return f'Customer: {self.name}, Balance: {self.balance}'

    def __eq__(self, other):
        return other is not None and \
            isinstance(other, Customer) and \
            self.__name == other.__name

class Bank:

    def __init__(self):
        self.__customers = []

    def add_customer(self, customer):
        if customer not in self.__customers:
            self.__customers.append(customer)

    def remove_customer(self, customer):
        if customer in self.__customers:
            self.__customers.remove(customer)

    def get_customer(self, name):
        for customer in self.__customers:
            if customer.name == name:
                return customer
        return None

    def transfer(self, sender, receiver, amount):
        if sender not in self.__customers or receiver not in self.__customers:
            raise Exception('Invalid sender or receiver')
        
        if sender.balance < amount:
            raise Exception('Insufficient funds')

        sender.withdraw(amount)
        receiver.deposit(amount)


    def __str__(self):
        customers_str = ', '.join(str(customer) for customer in self.__customers)
        return f'Bank: [{customers_str}]'

if __name__ == '__main__':
    c1 = Customer('Alice')
    c2 = Customer('Bob')
    c3 = Customer('Charlie')
    bank = Bank()
    bank.add_customer(c1)
    bank.add_customer(c2)
    bank.add_customer(c3)
    print(bank)
    bank.remove_customer(c2)
    print(bank)
    print(bank.get_customer('Alice'))
    print(bank.get_customer('Bob'))
    print(bank.get_customer('Charlie'))
    bank.get_customer('Alice').deposit(100)
    bank.get_customer('Charlie').deposit(200)
    print(bank.get_customer('Alice'))
    print(bank.get_customer('Charlie'))
    bank.transfer(bank.get_customer('Alice'), bank.get_customer('Charlie'), 50)
    print(bank.get_customer('Alice'))
    print(bank.get_customer('Charlie'))
    try:
        bank.transfer(bank.get_customer('Alice'), bank.get_customer('Charlie'), 100)
    except Exception as e:
        print(e)

    try:
        bank.transfer(bank.get_customer('Alice'), bank.get_customer('David'), 50)
    except Exception as e:
        print(e)
        
    try:
        bank.get_customer('Alice').withdraw(100)
    except Exception as e:
        print(e)
    
