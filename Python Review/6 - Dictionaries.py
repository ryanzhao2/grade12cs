# #Q1
# import random
# words = {}
# random_list = []
#
# for i in range(1,1001):
#     random_list.append(random.randint(1, 10))
#
# #  print(random_list)
#
# for char in random_list:
#     if char not in words:
#         words[char] = 1
#     elif char in words:
#         words[char] += 1
# sorted_keys = sorted(words)
# print(sorted_keys)
#
# for i in sorted_keys:
#     words[i] = f'{words[i] // 10}%'
#     print(f'num {i:>2}, chosen {words[i]:>3} time')

#Q2 method 1
# dict = {'JAN': 1,'FEB': 2,'MAR': 3, 'APR': 4,'MAY': 5, 'JUN': 6, 'JUL': 7,'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}
# def split_dict(date):
#     new_split = date.split('-')
#     month = dict[new_split[1]]
#     day = int(new_split[0])
#     year = int(new_split[2])
#     if year > 22:
#         year = 1900 + year
#     else:
#         year = 2000 + year
#     tup = (year, month, day)
#     return tup
#
# print(split_dict('8-MAR-85'))
# #Q2 method 2
# dict = {'JAN': 1,'FEB': 2,'MAR': 3, 'APR': 4,'MAY': 5, 'JUN': 6, 'JUL': 7,'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}
# def split_date(date):
#     split = date.split("-")
#     return split
#
# date = split_date('8-MAR-85')
# month = date[1]
# year = int(date[2])
#
# if year > 22:
#     year = 1900 + year
# else:
#     year = 2000 + year
#
# month_num = dict[month]
# print(f'{year}-{month}-{date[0]}')

#Q3
# import string
#
# dict = {}
# for i in string.ascii_lowercase:
#     unicode = ord(i) + 7
#     dict[i] = chr(unicode)
#
# print(dict['c'])

#Q4
# morse = {"A" : ".-", "B" : "-...", "C" : "-.-.", "D" : "-..", "E" : ".", "F" :
#     "..-.", "G" : "--.", "H" : "....", "I" : "..", "J" : ".---", "K" : "-.-", "L" :
#     ".-..", "M" : "--", "N" : "-.", "O" : "---", "P" : ".--.", "Q" : "--.-", "R" :
#     ".-.", "S" : "...", "T" : "-", "U" : "..-", "V" : "...-", "W" : ".--", "X" :
#     "-..-", "Y" : "-.--", "Z" : "--..", "0" : "-----", "1" : ".----", "2" :
#     "..---", "3" : "...--", "4" : "....-", "5" : ".....", "6" : "-....", "7" :
#     "--...", "8" : "---..", "9" : "----.", "." : ".-.-.-", "," : "--..--"," " : " "}
# code = '.... ..- -- .--. - -.--   -.. ..- -- .--. - -.--   ... .- -   --- -.   .-   .-- .- .-.. .-.. .-.-.-\
#   .... ..- -- .--. - -.--   -.. ..- -- .--. - -.--   .... .- -..   .-   --. .-. . .- -   ..-. .- .-.. .-.. .-.-.-\
#   .- .-.. .-..   - .... .   -.- .. -. --. ...   .... --- .-. ... . ...   .- -. -..   .- .-.. .-..   - .... .   -.- .. -. --. ...   -- . -. .-.-.-\
#   -.-. --- ..- .-.. -.. -. -   .--. ..- -   .... ..- -- .--. - -.--   - --- --. . - .... . .-.   .- --. .- .. -. .-.-.-'
# def reverse_dictionary(some_dict):
#     reverse_dict = {}
#
#     for key in some_dict.keys():
#         reverse_dict[some_dict[key]] = key
#     return reverse_dict
#
# reverse_morse = reverse_dictionary(morse)
# print(reverse_morse)
# split_code = code.split(" ")
# print(split_code)
#
# code_str = ''
# for char in split_code:
#     if char != '':
#         code_str +=reverse_morse[char]
#     else:
#         code_str += ' '
# print(code_str)

# #Q5
# price_list = [3.98, 0.97, 2.97, 3.99, 3.98, 1.98, 3.98, 1.98, 1.98, 3.98, 2.98,
#               2.99, 3.97, 0.97, 1.99, 0.98, 0.97, 3.99, 2.99, 3.97, 3.99, 0.98,
#               3.97, 1.98, 2.99, 1.97, 2.98, 1.97, 0.98, 2.97, 3.97, 0.99, 1.97,
#               2.97, 2.99, 1.98, 0.98, 1.98, 1.97, 1.98, 2.99, 1.97, 0.98, 0.97,
#               1.99, 3.97, 2.99, 0.99, 3.98, 3.97, 3.97, 1.99, 3.97, 3.98, 1.98,
#               2.99, 2.97, 3.97, 3.99, 3.98, 3.99, 2.97, 0.97, 0.99, 1.97, 0.97,
#               2.99, 3.99, 0.99, 2.97, 0.98, 3.97, 1.99, 0.99, 1.97, 0.97, 0.97,
#               2.99, 0.99, 0.97, 3.97, 1.99, 2.98, 3.97, 3.99]
# item_list = ['advil', 'aspirin', 'antacids', 'antibiotic ointment', 'anti-bacerial toweletters',
#              'automotive repair kits', 'baking tin', 'bandages', 'bandannas', 'baking soda', 'lighters',
#              'boxed food', 'bungee cords', 'cable ties', 'camping fuel', 'candles', 'canned fruits',
#              'canned meat', 'canned veggies', 'can openers', 'car towels', 'chewing gum', 'clothesline',
#              'coffee filters', 'combs', 'compact mirror', 'condiments', 'cotton balls', 'cokkie tins',
#              'cough drops', 'cutting boards', 'dental floss', 'digital thermometer', 'dish towels',
#              'dog food', 'duct tape', 'drop cloth', 'ear plugs', 'elastic hair bands',
#              'emergency cell phone chargers', 'epsom salts', 'eyeglass repair kit', 'facial tissues',
#              'gauze', 'gardening globes', 'hard candies', 'hydrogen peroxide', 'hand sanitizer',
#              'jarred foods', 'instant ice packs', 'knives', 'latex dishwashing gloves', 'lip balms',
#              'lotions', 'magnifying glass', 'matches', 'mesh laundry bag', 'nails', 'screws',
#              'plastic shoe container', 'rubbing alcohol', 'safety pins', 'salt with iodine',
#              'scrub buddies', 'sewing kit', 'shoe laces', 'soaps', 'socks', 'solar lights',
#              'spices', 'stell wool', 'sponges', 'sugar', 'super glue', 'sun hat', 'toothbrushes',
#              'tote bags', 'travel bottles', 'twine', 'utility pail', 'water', 'wet wipes']
#
# dict = {}
# item_price = list(zip(item_list, price_list))
# for char in item_price:
#     dict[char[0]] = char[1]
# print(dict)

#Q6
# d = {}
# for i in range(1, 7):
#     for j in range(1,7):
#         tup = (i, j)
#         sum = i + j
#         list = []
#         list.append(tup)
#         d[1] = list
#
# for char in d.keys():
#     print(char, d[char])
#
# print(f'Length: {len(d)}')

#######################################################################
#############  Working code for list of list ##########################
#######################################################################
# d = {}
# main_list = []
# ### create 12 seperate list inside of main_list
# for i in range(12):
#     main_list.append([])
#
# ######add the tuple to each of the 12 lists above
# for i in range(1, 7):
#     for j in range(1,7):
#         tup = (i, j)
#         sum = i + j
#         main_list[sum - 2].append(tup)   #### NOTE: sum -2, because main_list index starts from 0
# print(main_list)
# #### save the data in each list to individual dictionary
# for i in range(2, 13):
#     d[i] = main_list[i - 2]
#
# for char in d.keys():
#     print(char, d[char])
#
# print(f'Length: {len(d)}')
# ####################### the END ###################