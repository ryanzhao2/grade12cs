import random
words = {}
random_list = []
for i in range(1,1001):
    random_list.append(random.randint(0,9))

for char in random_list:
    if char not in words:
        words[char] = char
    #words[i] = i

#print(a)
print(words)