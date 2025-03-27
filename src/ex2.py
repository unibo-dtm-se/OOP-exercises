# Create a "Car" class with fields "producer", "model", and "year". 
# Include a method to display the details of the car as a string. 
# Include methods to compute the equality among cars.

class Car:

    def __init__(self, producer: str, model: str, year: int) -> None:
        self.__producer = producer
        self.__model = model
        self.__year = year

    @property
    def producer(self) -> str:
        return self.__producer

    @property
    def model(self) -> str:
        return self.__model

    @property
    def year(self) -> int:
        return self.__year
    
    def __str__(self) -> str:
        return f"Car -> {self.__producer} {self.__model} {self.__year}"

    def __eq__(self, other) -> bool:
        return other is not None and \
            isinstance(other, Car) and \
            self.__producer == other.producer and \
            self.__model == other.model and \
            self.__year == other.year

if __name__ == '__main__':
    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Toyota", "Corolla", 2020)
    car3 = Car("Toyota", "Corolla", 2021)
    car4 = Car("Toyota", "Camry", 2020)

    print(car1)
    print(car1 == car2)
    print(car1 == car3)
    print(car1 == car4)