'''
Given an array of integers, find the pair of 
adjacent elements that has the largest product 
and return that product.
Example: 
input -> list_1 = [3, 6, -2, -5, 7, 3]
output -> 21
'''

# list_1 = [3, 6, -2, -5, 7, 3]

# def get_max_product(arr):
#     max_product = arr[0] * arr[1]

#     for i in range(len(arr) - 1):
#         if arr[i] * arr[i + 1] > max_product:
#             max_product = arr[i] * arr[i + 1]

#     return max_product

# print(get_max_product(list_1))

'''
Write a program to generate this image and 
save this image in computer (use ImageGrab)
'''

# def print_triangle(n):
#     for i in range(n):
#         text = ""
#         for k in range(n - i - 1):
#             text += " "
#         for j in range(i + 1):
#             text += "* "
#         print(text)

# print_triangle(5)

'''
You are given an array prices where prices[i] is the price of a 
given stock on the i-th day.
You want to maximize your profit by choosing a single day 
to buy one stock and choosing a different day in the future 
to sell that stock.
Return the maximum profit you can achieve from this 
transaction and indexes of days (purchase, sell). If you 
cannot achieve any profit, return 0.
Example: price_list = [10, 2, 12, 5, 1, 7, 3, 2, 9, 5] 
-> profit = 10, day_start = 2, day_sell = 3
'''

# price_list = [10, 2, 12, 5, 1, 7, 3, 2, 9, 5] 

# def calculate_profit(arr):
#     day_start = 0
#     day_sell = 1
#     profit = 0
#     future_low = 0

#     for i in range(1, len(price_list)):
#         if i == 1 and arr[day_sell] < arr[day_start]:
#             day_start = day_sell
#             future_low = day_start

#         elif arr[i] < arr[future_low]:
#             future_low = i
        
#         elif arr[i] > arr[day_sell]:
#             day_sell = i
#             day_start = future_low

#         elif arr[i] - arr[future_low] > arr[day_sell] - arr[day_start]:
#             day_start = future_low
#             day_sell = i
            
#     profit = arr[day_sell] - arr[day_start]
#     print(f"start day - {day_start + 1}, price - {arr[day_start]}")
#     print(f"sell day - {day_sell + 1}, price - {arr[day_sell]}")
#     print(f"profit - {profit}")

# calculate_profit(price_list)



