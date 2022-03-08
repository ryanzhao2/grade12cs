# a = 'hello'
# print(a[-1])

# a = False or False or False or True
# print(a)
# print(bool(a))

#print(ord('u'))

# fruits = 'banana'
#
# if "ba2132131" in fruits:
#   print("yes")
#
# def sum13(nums):
#   sum_list = []
#   for i in range(len(nums)):
#     if i == 0 and nums[0] != 13:
#       sum_list.append(nums[i])
#     elif nums[i] != 13 and nums[i-1] != 13:
#       sum_list.append(nums[i])
#   return sum(sum_list)
#
# print(sum13([2,2,2,2,2,13,10,13,10,10]))
#
# dict = {'One': 1, 'Two': 2, 'Three': 3}
#
# dict[" "] = ""
#
# print(dict)
# def reverse_dictionary(some_dict):
#     reverse_dict = {}
#
#     for key in some_dict.keys():
#         reverse_dict[some_dict[key]] = key
#         print(some_dict)
#         print(some_dict[key])
#     return reverse_dict
#
# print(reverse_dictionary(dict))
#
# import string
#
#
# def count_word_frequency(some_text):
#     all_words = some_text.split()
#
#     word_frequency_dict = {}
#
#     for word in all_words:
#
#         for symbol in string.punctuation:
#             word = word.replace(symbol, "")
#
#         if word not in word_frequency_dict:
#             word_frequency_dict[word] = 1
#         else:
#             word_frequency_dict[word] += 1
#
#     return word_frequency_dict
#
#
# #MAIN
#
# text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris diam lacus, gravida in faucibus vitae, scelerisque ac libero. Donec eu risus elementum, luctus purus sit amet, hendrerit diam. Vestibulum eu odio iaculis nibh interdum consectetur non ac ex. Fusce eget faucibus nisl. Aliquam eu leo mi. Proin et laoreet ex, a molestie justo. Etiam odio sapien, facilisis aliquam sem vel, aliquet tempor nisl. Morbi at orci vestibulum, iaculis quam fermentum, vestibulum mi. Sed dapibus ipsum eget faucibus porta.\
# Vestibulum cursus, neque vitae commodo rutrum, augue tellus placerat lectus, sit amet iaculis massa diam a diam. Sed quis dolor maximus, pulvinar neque eget, hendrerit dui. Etiam sapien dolor, malesuada vel dui ac, vehicula cursus dui. Integer facilisis nisi quis diam gravida, sed semper libero mattis. Proin sollicitudin vehicula tortor eu suscipit. Cras ultrices feugiat tortor rutrum scelerisque. Suspendisse eget vulputate ex, ut vulputate leo. Nullam a justo fringilla, blandit lectus sit amet, tincidunt dolor. Proin efficitur vehicula leo et gravida.\
# Nulla egestas sapien quis odio hendrerit gravida. Suspendisse interdum ex sed sapien fermentum consequat. In ante orci, aliquam in diam at, semper ultrices tellus. Sed nec pharetra erat. Nulla ac suscipit ligula, aliquam commodo ipsum. Etiam tempor finibus euismod. Aliquam vehicula odio arcu, quis ornare dui fringilla pretium. Curabitur quis ligula non eros rutrum placerat. Morbi dapibus tempus facilisis. Sed lobortis faucibus pellentesque. Donec nec ante dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
# Nullam at blandit enim. Vestibulum ullamcorper pharetra tellus id lobortis. Sed non lacinia justo. Nulla tincidunt diam lectus, a molestie nisi mollis eget. Sed quis pretium sapien. Etiam ultricies risus a arcu facilisis volutpat. Pellentesque eget nisi sed lorem vehicula laoreet. Nunc et sem porta, hendrerit diam nec, imperdiet lorem. Sed tincidunt ullamcorper risus, eu lobortis leo porttitor eu. Sed lectus nisi, vehicula non vehicula interdum, venenatis aliquet tortor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. In purus lorem, facilisis sit amet diam at, hendrerit ornare libero. Quisque pharetra feugiat justo ut imperdiet. Suspendisse ac pulvinar nunc, in convallis mauris. Ut faucibus nunc at metus congue placerat. Praesent ac dolor ac tortor bibendum placerat sed sit amet ipsum.\
# Nunc porta enim a condimentum bibendum. In elit justo, placerat at neque nec, auctor placerat magna. Nulla bibendum nunc a risus vestibulum, eu elementum lacus sollicitudin. Sed suscipit convallis scelerisque. Nam eget scelerisque magna, quis lacinia diam. Nam ut lorem lobortis, dignissim urna convallis, laoreet sem. Suspendisse eget enim mattis, interdum justo a, egestas risus. Nulla nec magna ut risus auctor porttitor vitae eget nisi. Aenean massa eros, imperdiet eget finibus at, imperdiet blandit odio. Nam id condimentum lectus."
#
# word_count_dict = count_word_frequency(text)
#
# for key in sorted(word_count_dict):
#     print(key, word_count_dict[key])
#
# #
# a = 7
# print(a % 2)
#
# import math
#
# r = 5
#
# print(f'Arc length in a circle with radius {r} units')
#
# for degree in range(30, 360, 30):
#    arc = (degree / 360) * (2 * math.pi * r)
#
#    print(f'{r:>6} units {degree:>7} degree {arc:>10.2f} units')
# dict = {'red': 1}
# print(dict)
#
# dict['red'] = 2
# print(dict)
# list = [1, 5.0, '8']
# print(list)
#
# list2 = list
# list2.append(100)
# print(list)
# list3 = list.copy()
# list3.append(500)
# print(list3.index(500))
#
# def change(mylist):
#     mylist.append('hong')
#
#
# change(list3)
# print(list3[::-1])
#
#
#
import string
#
# str = "\n\n\n\t\t\t\t   12     3456"
# print(str.index('5'))
# print(str.strip())
#
# str2 = str.strip('15')
#
# # Python3 program for demonstration
# # of index() method
#
# list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]

# Will print index of '4' in sublist
# having index from 4 to 8.
# print(list1.index(4, 3, 8))
#
# def reverse_word(str):
#     new_str = ''
#     for i in range(len(str)-1, -1, -1):
#         new_str += str[i]
#     return new_str
#
# print(reverse_word('hello'))
#
# def password(str):
#     first = False
#     second = False
#     third = False
#     a = string.ascii_lowercase
#     b = string.ascii_uppercase
#     num = '0123456789'
#     for i in range(len(str)):
#         if str[i] in a:
#             first = True
#         elif str[i] in b:
#             second = True
#         elif str[i] in num:
#             third = True
#     return first and second and third
#
# print(password('Yishui$01'))
#
#
# for i  in range (4, 2, 4):
#     print (i)

# a = 'asdsad   sasdsad'
# print(a.strip('a'))
# a = int(1)
# print(a[-3:])
#
# print(type(a) == int)
# tup = (1,2,3,4)
# list = ['BENETNASCH,MIZAR', '12334324']
# print(tuple(list))
# print(tup)
# data = ['BENETNASCH,MIZAR', 'MERAK,DUBHE']
# tup = tuple(data)
# print(tup)
# for i in range(len(data)):
#     tup = tuple(data[i])
#     #data[i] = data[i]#, #'()'
# print(tup)
# #print(new_list)

#[:] makes a copy of the list
# list = [1,2,3,4,5]
# a = list[0:]
# list.append('hi')
# print(list)
# print(a)
def factorial( n ):
 if n > 1:
    result = n * factorial(n - 1)
    return result
 else:
    return 1
print(factorial(6))