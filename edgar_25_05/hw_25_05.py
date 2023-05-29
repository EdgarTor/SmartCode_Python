from string import ascii_lowercase

'''
1․ Գրել ֆունկցիա, որը․
   - տրված բառերի list-ը կֆիլտրի այնպես, որ կթողի միայն ամենաերկար բառերը
     (այսինքն՝ կգտնի ամենաերկար բառի երկարությունը և լիստում կթողնի միայն այդ 
     երկարության բառերը),
   օրինակ՝ input = ["aba", "aa", "z", "ad", "vcd", "aba"]
           output = ["aba", "vcd", "aba"],
           
           input = ["aba", "aa", "z", "advc", "vcd", "aba"]
           output = ["advc"],
   - վերջում գնահատեք Ձեր գրած կոդը Big O notation-ի միջոցով։
'''

# input_1 = ["aba", "aa", "z", "ad", "vcd", "aba"]
# input_2 = ["aba", "aa", "z", "advc", "vcd", "aba"]

# def get_long_words(arr):
#     unique_words = list(set(arr))
#     max_length = len(unique_words[0])

#     for word in unique_words:
#         if len(word) > max_length:
#             max_length = len(word)

#     new_list = list(filter(lambda word: len(word) == max_length, arr))

#     return new_list

# print(get_long_words(input_2)) # Big O - O(n)

'''
2․ Գրել ֆունկցիա, որը․
   - կհաշվի, թե տրված ամբողջ թվերի list-ից քանի քայլով կարելի է ստանալ մոնոտոն աճող թվերից բաղկացած list,
     մեկ քայլի ընթացքում թույլատրվում է թվերից մեկը մեկով մեծացնել, թվերի տեղերը փոխել չի կարելի, 
   օրինակ՝ [-10, 0, -2, 0] -> 5,
           [1, 1, 1] -> 3:
'''
# input_1 = [-10, 0, -2, 0]
# input_2 = [1, 1, 1]

# def get_monoton_increasing_list(arr):
#     steps = 0

#     for i in range(1, len(arr)):
#         if arr[i] <= arr[i-1]:
#             dif = abs(arr[i-1] - arr[i])
#             arr[i] += dif + 1
#             steps += dif + 1
                
#     return (arr, steps)

# print(get_monoton_increasing_list(input_2))

'''

3. Գրել ֆունկցիա, որը․
   - կստանա երկու արգումենտ՝ a և b,
   - կվերադարձնի a-ի b աստիճանի ամենավերջի թվանշանը,
   փորձել խնդիրը լուծել այնպես, որ կոդը աշխատի շատ արագ՝ նույնիսկ շատ 
   մեծ թվերի դեպքում։
'''

# def last_digit(a, b):
#     last_nums = {
#         0: 0,
#         1: 1,
#         2: {
#             1: 2,
#             2: 4,
#             3: 8,
#             4: 6
#         },
#         3: {
#             1: 3,
#             2: 9,
#             3: 7,
#             4: 1
#         },
#         4: {
#             1: 4,
#             2: 6,
#             3: 4,
#             4: 6
#         },
#         5: 5,
#         6: 6,
#         7: {
#             1: 7,
#             2: 9,
#             3: 3,
#             4: 1
#         },
#         8: {
#             1: 8,
#             2: 4,
#             3: 2,
#             4: 6
#         },
#         9: {
#             1: 9,
#             2: 1,
#             3: 9,
#             4: 1 
#         }
#     }
    
#     if b == 0:
#         return 1
#     elif b == 1:
#         return a % 10
#     else:
#         if a % 10 in [0, 1, 5, 6]:
#             return last_nums[a % 10]
#         if b % 4 == 0:
#             return last_nums[a % 10][4]
        
#         return last_nums[a % 10][b % 4]
    
# print(last_digit(9, 26))    

'''
Caesar cipher
'''

# def ceaser_cipher(text: str):
#     # [a, b, c, ....... x, y, z, a, b, c] 
#     text = text.lower()
#     ciphertext = ""

#     for letter in text:
#         if letter not in ascii_lowercase:
#             ciphertext += letter
#             continue

#         letter_index = ascii_lowercase.index(letter)
#         if letter_index + 3 <= 25:
#             ciphertext += ascii_lowercase[letter_index + 3]
#         else:
#             new_index = (letter_index + 3) % 25 - 1
#             ciphertext += ascii_lowercase[new_index]

#     return ciphertext

# print(ceaser_cipher("abc, xyz"))
        