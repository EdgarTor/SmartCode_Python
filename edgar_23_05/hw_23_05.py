from math import pi
import datetime

'''
1․ Գրել ֆունկցիա, որը․
   - որպես արգումենտ կընդունի շրջանագծի շառավիղը (r) և սեկտորի անկյունը 
   (alpha) ռադիաններով արտահայտված,
   - կհաշվի և կտպի համապատասխան շառավղով և անկյունով շրջանի մակերեսը,
   - բանաձևը՝ S = (pi * r ** 2) * alpha / 360, բանաձևի մեջ alpha-ն 
   արտահայտված է աստիճաններով։
'''

# def convert_rad_to_degree(alpha):
#     return alpha * 57.3

# def get_circle_area(radius, alpha):
#     s = (pi * radius ** 2) * convert_rad_to_degree(alpha) / 360

#     print(round(s, 2))

# get_circle_area(3, 1.5)

'''
2․ Գրել ծրագիր, որը․
   - կստանա 3 արգումենտ՝ տարի, ամիս, օր,
   - կտպի թե նշված օրն շաբաթվա որ օրն է։
'''

# def get_day_of_week(year, month, day):
#     days_of_week = {
#         0: "Monday",
#         1: "Tuesday",
#         2: "Wednesday",
#         3: "Thursday",
#         4: "Friday",
#         5: "Saturday",
#         6: "Sunday"
#     }
#     date = datetime.date(year, month, day)
#     day_index = date.weekday()

#     return days_of_week[day_index]

# print(get_day_of_week(2023, 5, 25))

'''
3․ Գրել ֆունկցիա, որը․
   - կստանա արգումենտ արաբական բնական թիվ (0-ից մեծ),
   - կվերադրձնի այդ թիվը հռոմեական տեսքով,
   հռոմեական թվերի համարժեքները՝ I-1, V-5, X-10, L-50, C-100, D-500, M-1000,
   օրինակ՝ 15 -> XV,
           72 -> LXXII,
           9 -> IX:
'''

# def convert_numbers_to_roman_numerals(num):
#     roman_numerals = {
#         1: "I",
#         4: "IV",
#         5: "V",
#         9: "IX",
#         10: "X",
#         50: "L",
#         100: "C",
#         500: "D",
#         1000: "M"
#     }

#     keys_list = list(roman_numerals.keys())
#     keys_list.reverse()

#     result = ""
#     for i in keys_list:
#         if num == i:
#             result += roman_numerals[i]
#             return result
        
#         if num // i > 0:
#             for _ in range(num // i):
#                 result += roman_numerals[i]
        
#         num = num % i

#     return result
            

# print(convert_numbers_to_roman_numerals(2112))
