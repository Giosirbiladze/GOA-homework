list_of_integers = [1, 2, 3, 4, 5]
print(list_of_integers[1:4])


#2)
numbers = [1, 2, 3, 4, 5, 6]
nums = numbers[0:3]
print(numbers[0:3])
new_list = []
new_list.append(nums)
print(new_list)


#3)
numbers_list = [1, 2, 3, 4, 5, 6]
x = numbers_list.index(1)
y = numbers_list.index(2)
z = numbers_list.index(3)
print(x, y, z)

#4)
list_of_integers = [1, 2, 3, 4, 5]
max_number = max(list_of_integers)
min_number = min(list_of_integers)
num1 = list_of_integers.index(max_number)
num2 = list_of_integers.index(min_number)
list_of_integers.pop(num1)
list_of_integers.pop(num2)
print(list_of_integers)

#5)
new_list = []
new_list.append(min_number)
new_list.append(max_number)
print(new_list)

#6)
nums1 = [1, 2, 3, 4, 5]
nums2 = [5, 6, 7, 8, 9]
max_num1 = max(nums1)
max_num2 = max(nums2)
min_num1 = min(nums1)
min_num2 = min(nums2)
A = max_num1 - min_num2
B = max_num2 - min_num1
new_list = []
new_list.append(A)
new_list.append(B)
print(new_list)


#7)
list_of_integers = [1, 2, 3, 4, 5]
print(sum(list_of_integers))

#8)
mixed_list = [1, 2, 'a', 3, 'b', 'c', 4, 'd']
list_of_integers = []
list_of_strings = []
for i in mixed_list:
  if type(i) == int:
    list_of_integers.append(i)
  if type(i) == str:
    list_of_strings.append(i)
    combined = ''.join(list_of_strings)
print(combined)
print(sum(list_of_integers))



#9)
nums1 = [1, 2, 3, 4, 5]
nums2 = [5, 6, 7, 8, 9]
sum_nums1 = sum(nums1)
sum_nums2 = sum(nums2)
x = sum_nums1 + sum_nums2
print(x)

fruits = ["Apples", "Bananas", "Oranges", "Mango", "Strawberries"]
reversed_fruits = []
for i in range(len(fruits) - 1,-1,-1):
  reversed_fruits.append(fruits[i])
print(reversed_fruits)


fruits = ["Apples", "Bananas", "Oranges", "Mango", "Strawberries"]
reversed_fruits = fruits[:: -1]
print(reversed_fruits)

list_of_integers = [1, 2, 3, 4, 5]
reversed_integers = []
for i in range(len(list_of_integers) - 1,-1,-1):
  reversed_integers.append(list_of_integers[i])
print(reversed_integers)

list_of_integers = [1, 2, 3, 4, 5]
reversed_integers = list_of_integers[:: -1]
print(reversed_integers)
