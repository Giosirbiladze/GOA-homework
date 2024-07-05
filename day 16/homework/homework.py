#max ფუნქციის კლონი 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

max_num = numbers[0]
for number in numbers:
    if max_num < number:
        max_num = number

print(max_num)


#min ფუნქციის კლონი 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

min_num = numbers[0]
for number in numbers:
    if max_num > number:
        min_num = number

print(min_num)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[1], numbers[-3], numbers[5])


numbers = [1, 2, 3, 4, 5]
fruits = ["Apples", "Bananas", "Oranges", "Mango", "Strawberries"]
new_list = []
length = max(len(numbers), len(fruits))
for i in range(length):
    if i < len(fruits):
     new_list.append(fruits[i])

    if i < len(numbers):
        new_list.append(numbers[i])
print(new_list)

mixed_list = [1, 2, 'a', 3, 'b', 'c', 4, 'd']
list_of_strings = []
list_of_integers = []
for i in mixed_list:
    if type(i) == str:
        list_of_strings.append(i)

    if type(i) == int:
        list_of_integers.append(i)
print(list_of_integers)
print(list_of_strings)


nums1 = [1, 2, 3, 4, 5]
nums2 = [5, 6, 7, 8, 9]
odd = []
even = []
for num1 in nums1:
    if num1 % 2 == 0:
        even.append(num1)
    else:
        odd.append(num1)
for num2 in nums2:
    if num2 % 2 == 0:
        even.append(num2)
    else:
        odd.append(num2)
print(sum(odd))
print(sum(even))

nums1 = [1, 2, 3, 4, 5]
nums2 = [5, 6, 7, 8, 9]
odd = []
even = []
for num1 in nums1:
    if num1 % 2 == 0:
        even.append(num1)
    else:
        odd.append(num1)
for num2 in nums2:
    if num2 % 2 == 0:
        even.append(num2)
    else:
        odd.append(num2)
print(odd)
print(even)

fruits = ["Apples", "Bananas", "Oranges", "Mango", "Strawberries"]
new_list = []
for i in fruits:
    new_list.append(len(i))
print(new_list)

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


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_index = []
for i in numbers:
    if numbers.index(i) % 2 == 0:
        even_index.append(i)
print(even_index)
