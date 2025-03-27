# Write a Python program to create a class representing a Poligon. 
# Include methods to calculate its area and perimeter.

class Polygon:
    def __init__(self, sides):
        """
        Initialize the polygon with a list of side lengths.
        :param sides: List of side lengths
        """
        self.sides = sides
    
    def perimeter(self):
        """
        Calculate the perimeter of the polygon.
        :return: Perimeter as the sum of all sides
        """
        return sum(self.sides)
    
    def area(self):
        """
        Placeholder for area calculation.
        Needs to be implemented in derived classes.
        """
        raise NotImplementedError("Area calculation must be implemented in a subclass")

# Example of a specific polygon: Rectangle
class Rectangle(Polygon):
    def __init__(self, width, height):
        """
        Initialize the rectangle with width and height.
        """
        super().__init__([width, height, width, height])
        self.width = width
        self.height = height
    
    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.width * self.height

if __name__ == '__main__':
    rectangle = Rectangle(5, 10)
    print("Perimeter:", rectangle.perimeter())  
    print("Area:", rectangle.area())