#Q1
# Generate three (3) test case scenarios for the function count_birthday_duplicate(month, day)
# Provided a birthday (Month Day   for example July 20)
#
# Loop to generate random birthday dates until the provided birthday is generated.
# Keep track of how many times it takes to generate the duplicate birthday.
#
# Return the number of times counted.

#Test Case 1 - Accurate count by generating the random birthday once
#result = count_birthday_duplicate('September', 27)
#print(result >= 1)

#Test Case 2 - Invalid Month
#result = count_birthday_duplicate('ABC', 31)
#print(result == 0)

#Test Case 3 - Invalid Day
#result = count_birthday_duplicate('July', 100)
#print(result == 0)

#Test Case 4 - Checking for leap year birthday
#result = count_birthday_duplicate('February', 29)
#print(result >= 1)
def encode_message(message):
    message = message.strip()
    if len(message) <= 1:
        return message.strip()
    else:
        message_list = list(message)
        message_list[0], message_list[-1] = message_list[-1], message_list[0]
        for i in range(0 , len(message_list)-1, 2):
            print(i)
            message_list[i], message_list[i+1] = message_list[i+1], message_list[i]

        x = ''.join(message_list)
        print(x)
        return x
    #print(message)




#Test Cases
print('\nTest case 1 - empty string')
result = encode_message('')
print(result == '')

print('\nTest case 2 - one character string')
result = encode_message('A')
print(result == 'A')

print('\nTest case 3 - one character + spaces')
result = encode_message('    A     ')
print(result == 'A')

print('\nTest case 4 - 4 characters and no space')
result = encode_message('GOLD')
print(result == 'ODGL')

print('\nTest case 5 - 3 characters and no space')
result = encode_message('GOL')
print(result == 'OLG')