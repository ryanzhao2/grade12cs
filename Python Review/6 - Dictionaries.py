#Q1
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
#
# sorted_keys = sorted(words.keys())
# for i in sorted_keys:
#     words[i] = f'{words[i] // 10}%'
#     print(f'num {i:>2}, chosen {words[i]:>3} time')

# #Q2
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
# print(f'{date[0]}-{month_num}-{year}')

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
