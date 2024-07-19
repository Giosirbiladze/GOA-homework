def function(num1):
    print(num1 + 5)
function(5)

def integers(num1, num2):
    print(num1 * num2)
integers(1, 100)

def string(word):
    print(len(word))
string("giorgi")

def list_of_string(*string_list):
    new_list = []
    for i in string_list:
        new_list.append(len(i))
    print(new_list)
list_of_string("apple", "banana", "cherry", "date")

def Palindrome(word):
    if word == word[::-1]:
        print("True")
    else:
        print("False")
Palindrome("wow")

def find_longest_string(*strings):
     longest_length = 0
     longest_string = ""
     for i in strings:
        if len(i) > longest_length:
            longest_length = len(i)
            longest_string = i
        print(longest_string)
find_longest_string("apple", "banana", "cherry", "date")

def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
print(factorial(5))

def max_sum_lists(list1, list2):
    max_list1 = max(list1)
    max_list2 = max(list2)
    sum_max = max_list1 + max_list2
    return [max_list1, max_list2], [sum_max]
list1 = [1, 5, 7, 3]
list2 = [9, 2, 4, 6]
result_lists = max_sum_lists(list1, list2)
print( result_lists[0])
print( result_lists[1])

def min_sum_lists(list1, list2):
    min_list1 = min(list1)
    min_list2 = min(list2)
    sum_min = min_list1 + min_list2
    return [min_list1, min_list2], [sum_min]
list1 = [1, 5, 7, 3]
list2 = [9, 2, 4, 6]
result_lists = max_sum_lists(list1, list2)
print( result_lists[0])
print( result_lists[1])

def sum_list(list1):
    max_list1 = max(list1)
    min_list1 = min(list1)
    sum = min_list1 - max_list1
    return  [sum]
list1 = [1, 5, 7, 3]
result_lists = sum_list(list1)
print( result_lists[0])




def sum_of_elements(nums):
    total = 0
    for num in nums:
        total += num
    return total
my_list = [1, 2, 3, 4, 5]
print(sum_of_elements(my_list))
 

def count_vowels(string):
    vowels = 'aeiou'
    vowel_count = 0
    for char in string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

def square_elements(nums):
    squared_list = [num ** 2 for num in nums]
    return squared_list
my_list = [1, 2, 3, 4, 5]
result_list = square_elements(my_list)
print(result_list) 

def reversing_string(str):
   reversed_string = str[::-1]
   print(reversed_string)
reversing_string("GIORGI")

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(is_even(4))

def longest_string(str_list):
    longest = max(str_list, key=len)
    return longest
strings = ['apple', 'banana', 'cherry', 'date']
print(longest_string(strings)) 

def smallest_number(numbers):
    if not numbers:
        return None
    return min(numbers)
numbers = [1, 2, 3, 4, 5]
print(smallest_number(numbers))

def divisor(*list_integers):
    sum1 = 1
    for i in list_integers:
        sum1 = sum1 * i
    print(sum1)
divisor(1, 2, 3, 4, 5)


def uppercase(input_str):
    return input_str.upper()
string = "Hello World!"
print(uppercase(string))

def average(*list_of_integers):
    print(sum(list_of_integers) / len(list_of_integers))
average(1, 2, 3, 4, 5)


