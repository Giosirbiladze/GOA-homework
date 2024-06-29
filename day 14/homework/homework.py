numbers = [1, 2, 3, 4, 5]
numbers.pop(4)
print(numbers[3])


fruits = ["Banana", "Apple", "Orange", "Dragon fruit"]
popped_fruit = fruits.pop(0)
fruits.append(popped_fruit)

char_list = ['a', 'b', 'c', 'd', 'e']
char_list.pop(2)

list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
popped_element = list_of_tuples.pop(2)
list_of_tuples.append(popped_element)

list = []
if list:
    last_element = list[1]
    list.pop(1)
else:
    print("Index Error there are no elements for pop! ")


numbers = [1, 5, 2, 5, 5, 3, 7, 5, 9]
number_5 = numbers.count(5)
print(number_5)


strings = ['a', 'b', 'c', 'd', 'a']
letter_a = strings.count('a')
print(letter_a)


boolean = [True, False, True, True, True]
true = boolean.count(True)
print(true)

nested_list = [[1, 2, 3], [3, 4], [3, 4]]
nested_3_4 = nested_list.count([3, 4])
print(nested_3_4)

numbers = [1, 5, 2, 5, 5, 3, 7, 5, 9]
max_number = max(numbers)
print(max_number)

fruits = ["Banana", "Apple", "Orange", "Dragon fruit"]
max_length = max(fruits)
print(max_length)

list_of_ages = [37, 48, 60, 12, 16, 23]
max_age = max(list_of_ages)
print(max_age)

datetime_list = [(2023, 6, 15),(2022, 8, 10),(2024, 2, 28),(2023, 12, 1)]
max_datetime = max(datetime_list)
print(max_datetime)

numbers = [1, 5, 2, 5, 5, 3, 7, 5, 9]
min_number = min(numbers)
print(min_number)

fruits = ["Banana", "Apple", "Orange", "Dragon fruit"]
min_length = min(fruits)
print(min_length)

temperatures = [22, 25, 18, 20, 15, 23, 21]
lowest_temperature = min(temperatures)
print(lowest_temperature)

product_list = [["product(1)", 50], ["product(2)", 100], ["product(3)", 150]]
low_price_product = min(product_list)
print(low_price_product)


numbers = [1, 5, 2, 5, 5, 3, 7, 5, 9]
sum_numbers = sum(numbers)
print(sum_numbers)

fruits = ["Banana", "Apple", "Orange", "Dragon fruit"]
strings_lenght = sum(len(i) for i in fruits)
print(strings_lenght)


game_result = [
    [1,0],
    [2,0],
    [0,1]
]
team_scores = []
for result in game_result:
    team_score = result[0]
    team_scores.append(team_score)
    
total = sum(team_scores)
print(total)

nestedarr = [
    [1,1],
    [1,1],
    [1,1]
]
total_count = []
total_sum = 0
for i in nestedarr:
    for j in i:
        total_sum += j
        total_count.append(total_sum)
        total_sum = 0
print(sum(total_count))

nestedarr = [
    [1,1],
    [1,1],
    [1,1]
]

total_length = 0
for i in nestedarr:
    total_length += len(i)

print(total_length)



integer_list = [3, 7, 12, 18, 25, 9, 14, 22, 31, 5]
list_length = len(integer_list)
print(list_length)


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
num_weekdays = len(weekdays)
print(num_weekdays)

A = "Giorgi"
length = len(A)
print(length)

#sum ფუნქციის კლონი
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

sum = 0
 
for number in numbers:
     sum = sum + number
    
print(sum)

#max ფუნქციის კლონი 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

max_num = numbers[0]
for number in numbers:
    if max_num < number:
        max_num = number

print(max_num)


#min ფუნქციის კლონი 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

min_num = numbers[0]
for number in numbers:
    if max_num > number:
        min_num = number

print(min_num)
