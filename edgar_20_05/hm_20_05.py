'''
1․ Գրել հետևյալ ծրագիրը․
   - բացել jupyter notebook-ը,
   - գեներացնել list, որը կպարունակի 1-ից 1000000 միջակայքում գտնվող կենտ թվերը,
   - պահել գեներացված list-ը համապատասխան ֆորմատով համակարգչի մեջ data անունով,
   - բացել pycharm-ը,
   - pycharm-ում կարդալ data ֆայլը,
   - կարդացած list-ում կթողնի միայն 3-ի բաժանվող թվերը,
   - կտպի ստացված list-ի արժեքների միջին թվաբանականը։
'''

# odd_nums = [i for i in range(1, 1000000, 2)]

# with open("data.txt", "w+") as file:
#     for num in odd_nums:
#         file.write(f"{num} ")
#    #  text = file.read()
#    #  print(text)

# with open("data.txt", "r") as f:
#     text = f.read()

# odd_nums_list = text.split()
# count = 0
# sum = 0

# for num in odd_nums_list:
#     if int(num) % 3 == 0:
#         count += 1
#         sum += int(num)

# print(sum / count)

'''
2․ Գրել ծրագիր, որը․
   - հետևյալ dict_1-ից կստանա նոր dict_2 այնպես, որ dict_2-ի key-երը լինեն 
   dict_1-ի value-ները, իսկ value-ները՝ dict_1-ի value-ների երկարությունները,
   օրինակ՝ dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'},
   պետք է ստացվի՝ dict_2 = {'red': 3, 'green': 5, 'black': 5, 'white': 5}:
'''

# dict_1 = {
#     1: 'red',
#     2: 'green',
#     3: 'black',
#     4: 'white',
#     5: 'black'
# }

# def get_new_dict(dict):
#     temp_dict = {}

#     for key in dict:
#         new_key = dict[key]
#         temp_dict[new_key] = len(new_key)

#     return temp_dict

# dict_2 = get_new_dict(dict_1)
# print(dict_2)

'''
3. Գրել ֆունկցիա, որը․
   - կֆիլտրի տրված dictionary-ի value-ները, թողնելով միայն կենտ թվերը,
   - կվերադարձնի ստացված dictionary-ն,
   օրինակ՝ {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]},
   պետք է ստացվի՝ {'a': [1, 3, 7], 'b': [], 'c': [9, 9, 5]}:
'''

# dict_1 = {
#     'a': [1, 8, 3, 7, 2],
#     'b': [12, 4, 8, 4],
#     'c': [9, 9, 2, 8, 5]
# }

# def get_dict_with_odd_values(dict):
#     for key in dict:
#         dict[key] = list(filter(lambda x: x % 2 == 1, dict[key]))

#     return dict

# dict_2 = get_dict_with_odd_values(dict_1)
# print(dict_2)
