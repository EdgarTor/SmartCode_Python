from abc import ABC, abstractmethod
from math import pi, sin

'''
1․ Գրել Shape abstract class, որը․
   - կունենա __init__(), perimetr(), area() աբստրակտ մեթոդներ։
2․ Գրել Circle class, որը կժառանգի Shape class-ից, որը․
   - __init__() -ում կընդունի շրջանագծի շառավիղը,
   - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտը ճիշտ մուտքագրված 
   լինի (պետք է լինի դրական թիվ),
   - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները շրջանագծի 
   համար։
3․ Գրել Rectangle class, որը կժառանգի Shape class-ից, որը․
   - __init__() -ում կընդունի ուղղանկյան լայնությունը և երկարությունը,
   - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ 
   մուտքագրված լինեն (պետք է լինեն դրական թվեր),
   - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները ուղղանկյան 
   համար։
4․ Գրել Triangle class, որը կժառանգի Shape class-ից, որը․
   - __init__() -ում կընդունի 
     -- կամ եռանկյան երեք կողմերը,
     -- կամ մեկ կողմը և բարձրությունը,
     -- կամ երկու կողմերը և այդ կողմերի կազմած անկյունը, 
   - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ 
   մուտքագրված լինեն,
   - կվերախմբագրի Shape class-ի perimetr() մեթոդը եռանկյան համար,
   - եռանկյան մակերեսը կհաշվի 3 տարբերակով, կախված մուտքագրված 
   պարամետրերից․
     1) S = (p * (p - a) * (p - b) * (p - c)) ^ 0.5   , որտեղ a, b, c - եռանկյան կողմերն են, p - եռանկյան կիսապարագիծը,
     2) S = a * h / 2                                 , որտեղ a - եռանկյան կողմը, h = եռանկյան բարձրությունը,
     3) S = a * b * sin(alpha) / 2                    , որտեղ a, b - եռանկյան կողմերն են, alpha - եռանկյան a և b կողմերի կազմած անկյունը։
'''

class Shape(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def perimetr():
        pass

    @abstractmethod
    def area():
        pass

class Validator:
    @staticmethod
    def is_valid(num: int | float) -> bool:
        return isinstance(num, (int, float)) and num > 0


class Circle(Shape, Validator):
    def __init__(self, radius: int | float):
        if self.is_valid(radius):
            self.radius = radius
        else:
            raise Exception("Invalid radius")

    def perimetr(self) -> int | float:
        return 2 * pi * self.radius
    
    def area(self) -> int | float:
        return 2 * pi * self.radius ** 2
    
    
class Rectangle(Shape, Validator):
    def __init__(self, length, width):
        if self.is_valid(length) and self.is_valid(width):
            self.length = length
            self.width = width
        else:
            raise Exception("Invalid sides")
        
    def perimetr(self) -> int | float:
        return 2 * self.length + 2 * self.width
    
    def area(self) -> int | float:
        return self.length * self.width
    
class Triangle(Shape, Validator):
    def __init__(self, side_a: int | float, side_b: int | float, side_c: int | float):
        if self.is_valid_triangle(side_a, side_b, side_c):
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c

    def is_valid_triangle(self, a: int | float, b: int | float, c: int | float):
        if self.is_valid(a) and self.is_valid(b) and self.is_valid(c):
            return a + b > c and a + c > b and b + c > a
        else:
            raise Exception("Invalid side")
        
    def perimetr(self):
        return self.side_a + self.side_b + self.side_c

    def area(self, side_a=None, side_b=None, h=None, alpha=None):
        if (side_a is not None) and (h is not None):
            return side_a * h / 2  
        elif (side_a is not None) and (side_b is not None) and (alpha is not None):
            return side_a * side_b * sin(alpha) / 2   
        else:
            p = self.perimetr() / 2
            return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5

