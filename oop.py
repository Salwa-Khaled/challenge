from abc import ABC, abstractmethod

class Shape(ABC): #abstract class
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side): #constructor
        self.__side = side    #encapsloetin value (praivet)

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return self.__side * 4

class Rect(Shape):            #inheret class
    def __init__(self, legth, width):
        self.__length = legth
        self.__width = width

    def area(self):           #polymphism(overriding)
        return self.__length * self.__width

    def perimeter(self):
        return (self.__length + self.__width) * 2

square = Square(10) #object from class
print(f"square area is {square.area()} and perimeter is {square.perimeter()}")

rect = Rect(3, 5)
print(f"rect area is {rect.area()} and perimeter is {rect.perimeter()}")
