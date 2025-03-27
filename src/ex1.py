# Create a class "Greeter" with a method "greet(...)" that prints a greeting for some name 
# to be provided as an argument.

class Greeter:
    def greet(self, name):
        print(f"Hello, {name}!")

if __name__ == '__main__':

    greeter = Greeter()
    greeter.greet("Davide")
    greeter.greet("Giovanni")
    greeter.greet("Francesca")