# a = 'hello'
# print(a[-1])

# a = False or False or False or True
# print(a)
# print(bool(a))

#print(ord('u'))

fruits = 'banana'

if "ba2132131" in fruits:
  print("yes")

def sum13(nums):
  sum_list = []
  for i in range(len(nums)):
    if i == 0 and nums[0] != 13:
      sum_list.append(nums[i])
    elif nums[i] != 13 and nums[i-1] != 13:
      sum_list.append(nums[i])
  return sum(sum_list)

print(sum13([2,2,2,2,2,13,10,13,10,10]))