'''
1․ Գրել BankUser class, որը․
   - __init__() -ում կընդունի մարդու անունը, ազգանունը, տարիքը, հաշվեհամարը, 
   գումարը հաշվեհամարի վրա, գաղտնաբառը,
   - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ են 
   մուտքագրված՝
     -- անունը և ազգանունը - տառերից բաղկացած,
     -- տարիքը - ամբողջ թիվ,
     -- հաշվեհամարը - 16 թվանշանից բաղկացած (xxxx xxxx xxxx xxxx կամ 
     xxxxxxxxxxxxxxxx ֆորմատով),
     -- գումարը - դրական թիվ,
     -- գաղտնաբառը - ամենաքիչը 8 սիմվոլից բաղկացած տեքստ,
   - անունը, ազգանունը և տարիքը կլինեն այնպիսի ատրիբուտներ, որոնց ուղիղ 
   հասանելիությունը կլինի պաշտպանված,
   - հաշվեհամարը, գումարը և գաղտնաբառը կլինեն այնպիսի ատրիբուտներ, որոնց 
   ուղիղ հասանելիությունը կլինի արգելված,   
   - կունենա մեթոդ, որը կվերադարձնի մարդու անունը և ազգանունը,
   - կունենա մեթոդ, որը կվերադարձնի մարդու տարիքը,
   - կունենա մեթոդ, որը կվերադարձնի հաշվեհամարը և գումարը, բայց միայն ճիշտ 
   գաղտնաբառ հավաքելուց հետո,
   - կունենա մեթոդ, որը կավելացնի գումար հաշվին,
   - կունենա մեթոդ, որը կհանի գումար հաշվից, հաշվի առեք, որ գումարը 
   բացասական չի կարող լինել։
'''

class BankUser:

    def __init__(self, first_name, last_name, age, card_number, amount, password) -> None:
        if not (self.is_only_letters(first_name) and self.is_only_letters(last_name)):
            raise Exception("First name and Last name should contain only letters")
        elif not self.is_valid_age(age):
            raise Exception("Age should be integer and greater than 0")
        elif not self.is_valid_card_number(card_number):
            raise Exception("Invalid card number")
        elif not self.is_valid_amount(amount):
            raise Exception("Invalid amount")
        elif not self.is_valid_password(password):
            raise Exception("Invalid password")
        else:
            self._first_name = first_name
            self._last_name = last_name
            self._age = age
            self.__card_number = card_number
            self.__amount = amount
            self.__password = password

    @staticmethod
    def is_only_letters(text):
        return text.isalpha()
    
    @staticmethod
    def is_valid_age(num):
        return num > 0 and type(num) == int
    
    @staticmethod
    def is_valid_card_number(card_number):
        if " " in card_number:
            card_number_list = card_number.split()

            if len(card_number_list) == 4:
                for item in card_number_list:
                    if not (len(item) == 4 and type(item) == int):
                        return False

            return False
        else:
            if not (len(card_number) == 16 and type(item) == int):
               return False
            
        return True
    
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0
    
    @staticmethod
    def is_valid_password(password):
        return len(password) >= 8 and type(password) == str
    
    def get_user_name(self):
        return f"{self._first_name} {self._last_name}"
    
    def get_user_age(self):
        return self._age
    
    def get_card_number_and_amount(self):
        psw = input("input password")
        if psw == self.__password:
            return f"{self.__card_number}, {self.__amount}"
        else:
            raise Exception("Invalid password")
        
    def add_amount(self, amount):
        self.__amount += amount

    def withdraw_amount(self, amount):
        if self.__amount - amount >= 0:
            self.__amount -= amount
        else:
            raise Exception("No enough amount")

