#This function only checks the if the first character is lowercase as it returns True or False after the first iteration of the loop
# def any_lowercase1(s):
#     for c in s:
#         if c.islower():
#             return True
#         else:
#             return False
# print(any_lowercase1('Hello'))

#This function checks if the string 'c' is lower so it will always return True
# def any_lowercase2(s):
#     for c in s:
#         if 'c'.islower():
#             return 'True'
#         else:
#             return 'False'
#
# print(any_lowercase2('Hello'))

#This function checks every letter of the string but only returns a boolean value based on the last character
# def any_lowercase3(s):
#     for c in s:
#         flag = c.islower()
#     return flag
# print(any_lowercase3('Hello'))

#This function uses a loop and an or statement to check
#if character in the string is lowercase or
#uppercase. When it finds that a character is lowercase,
#c.islower() will equal to true and flag will be assigned to True
#since it is assigned to the first object that is True or
#the last object in the expression regardless of it's truth value(which is c.islower() aswell)
#After flag is assigned to True, it will continue to be True as it is the first object that is True

# def any_lowercase4(s):
#     flag = False
#     for c in s:
#         flag = flag or c.islower()
#     return flag
# print(any_lowercase4('Hello'))
#
# #This function will continue to check to see if the characters of the string are lowercase
# #until it reaches a uppercase letter where it stops and returns False without
# #checking the rest of the characters which makes it inaccurate
# def any_lowercase5(s):
#     for c in s:
#         if not c.islower():
#             return False
#     return True
# print(any_lowercase5('hEllo'))

#Q2
# def is_palindrome(str):
#     if str == str[::-1]:
#         return True
#     return False
#
# print(is_palindrome('Yes'))

#Q3

# def rotate_word(str, rotation):
#     new_str = ''
#     for i in range(len(str)):
#         numeric_code = ord(str[i])
#         new_character = chr(numeric_code+rotation)
#         new_str += new_character
#     return new_str
#
# print(rotate_word('melon', -10))
