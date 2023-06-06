'''
1․ Գրել Triangle class, որը․
   - __init__() -ում կընդունի եռանկյան կողմերը և կստուգի արդյոք նման կողմերով 
   եռանկյուն գոյություն ունի թե ոչ,
     եթե կողմերը սխալ են տրված կվերադարձնի Error համապատասխան տեքստով,
   - կունենա մեթոդ, որը կվերադարձնի եռանկյան կողմերը,
   - կունենա մեթոդ, որը կվերադարձնի եռանկյան պարագիծը,
   - կունենա մեթոդ, որը կվերադարձնի եռանկյան մակերեսը,
   - կունենա մեթոդ, որը կվերադարձնի արդյոք եռանկյունը հավասարակողմ է, 
   հավասարասրուն, թե անկանոն (կողմերը իրար = չեն)։
'''

class Triangle:
    def __init__(self, side_1: int, side_2: int, side_3: int):
        if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 \
            and  side_2 + side_3 > side_1:

            self.side_1 = side_1
            self.side_2 = side_2
            self.side_3 = side_3
        else:
            raise Exception("Can not create a triangle with provided values")
        
    def get_sides(self) -> str:
        return f"side 1: {self.side_1}, side 2: {self.side_2}, " + \
                f"side 3: {self.side_3}"
    
    def get_perimeter(self) -> int:
        return self.side_1 + self.side_2 + self.side_3
    
    def get_area(self) -> float:
        s = self.get_perimeter() / 2
        area = (s * (s - self.side_1) * (s - self.side_2) * (s - self.side_3)) ** 0.5
        
        return round(area, 1)   

    def get_type(self) -> str:
        if self.side_1 == self.side_2 and self.side_2 == self.side_3:
            return "Equilateral triangle"
        elif self.side_1 == self.side_2 or self.side_2 == self.side_3 \
                or self.side_1 == self.side_3:
            return "Isosceles triangle"
        else:
            return "Scalene triangle"

        
# t = Triangle(7, 8, 9)
# print(t.get_sides())
# print(t.get_perimeter())
# print(t.get_area())
# print(t.get_type())

class Vector:
    MIN_VALUE = 0
    MAX_VALUE = 100

    def __init__(self, x: int, y: int):
        if self.validate(x, y):
            self.x = x
            self.y = y
        else:
            raise Exception("Butut")
    
    @staticmethod
    def validate(x, y):
        if 0 < x < 100 and 0 < y < 100:
            return True
        else:
            return False

v = Vector(1, 2)
v.validate()



