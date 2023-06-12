
'''
1․ Գրել Calculator class, որը․
   - __init__ ում կստանա թիվ և կստուգի այդ թվի int կամ float լինելը, հակառակ դեպքում կվերադարձնի Error,
   - կունենա միայն getter մեթոդ տրված թիվը ստանալու համար, իսկ այդ թիվը կլինի private,
   - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+, -, *, /, //, %, **),
   - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+=, -=, *=, /=, //=, %=, **=),
   - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (==, >, >=, <, <=, !=),
   - վերոնշյալ մեթոդները ռեալիզացված կլինեն այնպես, որ աշխատեն նաև Calculator կլասի երկու օբյեկտների համար,
   - կունենա համապատասխան magic մեթոդներ, որոնք թույլ կտան օբյեկտը տպելուց․ ստանալ թիվը (__str__), ստանալ թիվը և թվի տիպը (__repr__)։
'''

class Calculator:
    def __init__(self, number: int | float):
        if self.is_valid_number(number):
            self.__number = number
        else:
            raise Exception("Number should be int or float")

    @staticmethod
    def is_valid_number(num: int | float) -> bool:
        return isinstance(num, (int, float))
    
    @property
    def number(self):
        return self.__number
    
    def __add__(self, other):
        if self.is_valid_number(other):
            return Calculator(self.__number + other)
        elif isinstance(other, Calculator):
            return Calculator(self.__number + other.number)
        else:
            raise TypeError(f"{other} should be int, float or Calculator, not {type(other)}")
        
    def __radd__(self, other):
        return self + other
    
    def __iadd__(self, other):
        if self.is_valid_number(other):
            self.__number += other
        elif isinstance(other, Calculator):
            self.__number += other.number
        else:
            raise TypeError(f"{other} should be int, float or Calculator, not {type(other)}")
        
        return self
    
    def __sub__(self, other):
        if self.is_valid_number(other):
            return Calculator(self.__number - other)
        elif isinstance(other, Calculator):
            return Calculator(self.__number - other.number)
        else:
            raise TypeError(f"{other} should be int, float or Calculator, not {type(other)}")
        
    def __rsub__(self, other):

        # if other < 0 and self.__number > 0:
        #     return Calculator(self.__number * -1 + other)
        # elif self.__number < 0:
        #     return Calculator(other - self.__number)
        
        # return Calculator(-1 * (self.__number - other))

        return Calculator(other - self.__number)
    
    def __isub__(self, other):
        if self.is_valid_number(other):
            self.__number -= other
        elif isinstance(other, Calculator):
            self.__number -= other.number
        else:
            raise TypeError(f"{other} should be int, float or Calculator, not {type(other)}")
        
        return self

    def __mul__(self, other):
        if self.is_valid_number(other):
            return Calculator(self.__number * other)
        elif isinstance(other, Calculator):
            return Calculator(self.__number * other.number)
        else:
            raise TypeError(f"{other} should be int, float or Calculator, not {type(other)}")
        
    def __rmul__(self, other):
        return self * other
    
    def __imul__(self, other):
        if self.is_valid_number(other):
            self.__number *= other
        elif isinstance(other, Calculator):
            self.__number *= other.number
        else:
            raise TypeError(f"{other} should be int, float or Calculator, not {type(other)}")
        
        return self
    
    def __truediv__(self, other):
        if self.is_valid_number(other):
            return Calculator(self.__number / other)
        elif isinstance(other, Calculator):
            return Calculator(self.__number / other.number)
        else:
            raise TypeError(f"{other} should be int, float or Calculator, not {type(other)}")
        
    def __rtruediv__(self, other):
        return Calculator(other / self.__number)
    
    def __itruediv__(self, other):
        if self.is_valid_number(other):
            self.__number /= other
        elif isinstance(other, Calculator):
            self.__number /= other.number
        else:
            raise TypeError(f"{other} should be int, float or Calculator, not {type(other)}")
        
        return self
    
    def __floordiv__(self, other):
        if self.is_valid_number(other):
            return Calculator(self.__number // other)
        elif isinstance(other, Calculator):
            return Calculator(self.__number // other.number)
        else:
            raise TypeError(f"{other} should be int, float or Calculator, not {type(other)}")
        
    def __rfloordiv__(self, other):
        return Calculator(other // self.__number)
    
    def __ifloordiv__(self, other):
        if self.is_valid_number(other):
            self.__number //= other
        elif isinstance(other, Calculator):
            self.__number //= other.number
        else:
            raise TypeError(f"{other} should be int, float or Calculator, not {type(other)}")
        
        return self
    
    def __mod__(self, other):
        if self.is_valid_number(other):
            return Calculator(self.__number % other)
        elif isinstance(other, Calculator):
            return Calculator(self.__number % other.number)
        else:
            raise TypeError(f"{other} should be int, float or Calculator, not {type(other)}")
        
    def __rmod__(self, other):
        return Calculator(other % self.__number)
    
    def __imod__(self, other):
        if self.is_valid_number(other):
            self.__number %= other
        elif isinstance(other, Calculator):
            self.__number %= other.number
        else:
            raise TypeError(f"{other} should be int, float or Calculator, not {type(other)}")
        
        return self
    
    def __pow__(self, other):
        if self.is_valid_number(other):
            return Calculator(self.__number % other)
        elif isinstance(other, Calculator):
            return Calculator(self.__number % other.number)
        else:
            raise TypeError(f"{other} should be int, float or Calculator, not {type(other)}")
        
    def __rpow__(self, other):
        return Calculator(other **  self.__number)
    
    def __ipow__(self, other):
        if self.is_valid_number(other):
            self.__number **= other
        elif isinstance(other, Calculator):
            self.__number **= other.number
        else:
            raise TypeError(f"{other} should be int, float or Calculator, not {type(other)}")
        
        return self
    
    def __eq__(self, other):
        if self.is_valid_number(other):
            return self.__number == other
        elif isinstance(other, Calculator):
            return self.__number == other.number
        else:
            raise TypeError(f"{other} should be int, float or Calculator, not {type(other)}")
        
    def __lt__(self, other):
        if self.is_valid_number(other):
            return self.__number < other
        elif isinstance(other, Calculator):
            return self.__number < other.number
        else:
            raise TypeError(f"{other} should be int, float or Calculator, not {type(other)}")

    def __le__(self, other):
        if self.is_valid_number(other):
            return self.__number <= other
        elif isinstance(other, Calculator):
            return self.__number <= other.number
        else:
            raise TypeError(f"{other} should be int, float or Calculator, not {type(other)}")
        
    def __str__(self):
        return f"Object number is {self.__number}"
    
    def __repr__(self):
        return f" {self.__number}: {self.__class__}"


c1 = Calculator(2)
c2 = Calculator(3)

c2 **= c1

print(repr(c2))