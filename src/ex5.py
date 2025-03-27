# Write a Python program to create a class representing a shopping cart. 
# Include methods for adding and removing items, and calculating the total price.
# Items may require their own modelling as a class.

class Item:
    
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f"Item: {self.__name}, Price: {self.__price}"
    
    def __eq__(self, other):
        return other is not None and \
            isinstance(other, Item) and \
            self.__name == other.__name and \
            self.__price == other.__price

class ShoppingCart:
    
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, item):
        self.__items.remove(item)

    def total_price(self):
        return sum([item.price for item in self.__items])

    def __str__(self):
        items_str = ", ".join(str(item) for item in self.__items)
        return f"Items: [{items_str}], Total Price: {self.total_price()}"
    

if __name__ == '__main__':
    i1 = Item("Apple", 1.0)
    i2 = Item("Banana", 2.0)
    i3 = Item("Orange", 3.0)
    cart = ShoppingCart()
    cart.add_item(i1)
    cart.add_item(i2)
    cart.add_item(i3)
    print(cart.total_price())
    cart.remove_item(i2)
    print(cart.total_price())
    print(cart)