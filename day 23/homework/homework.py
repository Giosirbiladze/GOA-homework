def function(num1, num2):
    print(num1 + num2)
    print(num1 / num2)
    print(num1 * num2)
    print(num1 - num2)
function(25, 5)

def sum_up_to_100(num1, num2):
    while num1 <= 100:
        num1 += num2
    return num1
print(sum_up_to_100(20, 30)) 

def check_even_or_odd(number):
    if number % 2 == 0:
        return "რიცხვი ლუწია"
    else:
        return "რიცხვი კენტია"
print(check_even_or_odd(10))

def max_number(*numbers):
    print(max(numbers))
max_number(1, 2, 3, 4, 5)

def sum_number(*numbers):
    print(sum(numbers))
sum_number(1, 2, 3, 4, 5)

def function(*List):
    print(List[::-1])
function(1, "gio", "Cherry", 3, 4)

def list_strings(*list_of_strings):
    print((max(list_of_strings)))
    print((min(list_of_strings)))
list_strings('apple', 'banana', 'cherry', 'date')

def swap_case(*input_string):
    swapped_string = ""
    for i in input_string:
        if i.islower():
            swapped_string += i.upper()
        elif i.isupper():
            swapped_string += i.lower()
        else:
            swapped_string += i  
    return swapped_string

print(swap_case('apple', 'banana', 'cherry', 'date'))

def count_vowels(string):
    vowels = 'aeiou'
    vowel_count = 0
    for i in string:
        if i in vowels:
            vowel_count += 1
    return vowel_count
print(count_vowels('apple'))

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(is_even(4))

def sum_even_index(numbers):
    total = 0
    for i in range(len(numbers)):
        if i % 2 == 0:  
            total += numbers[i]
    return total


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_even_index(nums))

def check_even_odd(number):
    if number % 2 == 0:
        return "ლუწია"
    else:
        return "კენტია"
print(check_even_odd(10))

def capitalize_names(name_list):
    capitalized_names = [name.upper() for name in name_list]
    return capitalized_names


names = ["gio", "dima", "mate"]
updated_names = capitalize_names(names)
print(updated_names)



def transform_numbers(numbers):
    updated_numbers = []
    for num in numbers:
        if num % 2 == 0: 
            updated_numbers.append(num * 2)
        else:  
            updated_numbers.append(num // 2)
    return updated_numbers


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
updated_numbers = transform_numbers(numbers)
print(updated_numbers)

def swap_case(*input_string):
    swapped_string = ""
    for i in input_string:
        if i.islower():
            swapped_string += i.upper()
        elif i.isupper():
            swapped_string += i.lower()
        else:
            swapped_string += i  
    reversed = swapped_string[::-1]
    return reversed

print(swap_case('apple', 'banana', 'cherry', 'date'))

def categorize_strings(string_list):
    odd = []
    even = []

    for string in string_list:
        if len(string) % 2 == 1:  
            odd.append(string.upper())
        else:  
            even.append(string.upper())

    return odd, even


strings = ["dato", "nika",  "zaza", "tamar", "gio", "luka"]
odd_strings, even_strings = categorize_strings(strings)

print(odd_strings)
print(even_strings)  

def process_strings(string_list):
    new_list = []

    for string in string_list:
        
        even_count = sum(1 for char in string if char.isalpha() and ord(char) % 2 == 0)

        if even_count % 2 == 1:  
            new_list.append(string.upper())  
        else:
            new_list.append(string.capitalize())  

    return new_list


strings = ["dato", "nika", "zaza", "tamar", "gio", "luka"]
processed_list = process_strings(strings)

print("Processed list:")
for item in processed_list:
    print(item)

def findstring(s):
    index = 0
    for i in range(len(s)):
        index = i
    if index % 2 == 0:
        return s.upper()
    else:
        return s.capitalize()

print(findstring("gocha"))