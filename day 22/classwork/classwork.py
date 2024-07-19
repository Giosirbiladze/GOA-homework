def Calculate_average(*numbers):
    print( sum(numbers) / len(numbers))
Calculate_average(1, 2, 3, 4, 5)

def manual_sum(*numbers):
    sum1 = 0
    for number in numbers:
     sum1 = sum1 + number
     
manual_sum(1, 2, 3, 4, 5)


def greet():
   print("hello guest")
greet()

def nums(firstnum,secondnum):
   sum = 0
   for i in range(firstnum,secondnum):
      sum = sum + i 
      print(sum)
nums(1, 10)

def list_integers(*numbers):
    odd = []
    even = []
    for num1 in numbers:
     if num1 % 2 == 0:
        even.append(num1)
     else:
        odd.append(num1)
     print(odd)
     print(even)
list_integers(1, 2, 3, 4, 5)

def print_numbers(n):
   for i in range(1, n):
      print(i)
print_numbers(10)

def print_even_numbers(n):
   even = []
   for i in range(2, n):
      if i % 2 == 0:
         even.append(i)
   print(even)
print_even_numbers(10)

def sum(num1, num2):
   print(num1 + num2)
sum(1, 10)

def sum1(num1, num2):
   return(num1 + num2)
sum1(1, 100)

def joined_string(str1, str2):
   print(str1 + str2)
joined_string("gio", "rgi")

def find_maximum(num1, num2):
   if num1 > num2:
      print(num1)
   else:
      print(num2)
find_maximum(10, 20)

def reversing_string(str):
   reversed_string = str[::-1]
   print(reversed_string)
reversing_string("GIORGI")

def area(Length, width):
   print(Length * width)
area(10, 30)

def sum_of_numbers(*numbers):
   total_sum = 0
   for num in numbers:
    total_sum += num   
    return total_sum
   print(total_sum)
sum_of_numbers(1, 2, 3, 4, 5)

def count_vowels(string):
    vowels = 'aeiou'
    vowel_count = 0
    for char in string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

def capitalize_strings(strings):
    capitalized = []
    for string in strings:
        capitalized.append(string.upper())
    return capitalized
input_strings = ["apple", "banana", "cherry", "date"]
result = capitalize_strings(input_strings)
print(result)





