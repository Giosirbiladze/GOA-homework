def bumps(road):
    return "Woohoo!" if road.count('n') <= 15 else "Car Dead"

def greet(name): 
    return f"Hello {name.capitalize()}!"

def sum_even_numbers(seq): 
    return sum(x for x in seq if isinstance(x, int) and x % 2 == 0)

def reverse(lst):
    reversed_list = list(lst)
    n = len(reversed_list)
    for i in range(n // 2):
        reversed_list[i], reversed_list[n - 1 - i] = reversed_list[n - 1 - i], reversed_list[i]
    return reversed_list


def averages(arr):
    if len(arr) < 2:
        return []
    
    return [(arr[i] + arr[i + 1]) / 2 for i in range(len(arr) - 1)]


def add(num1, num2):
    result = 0
    multiplier = 1
    
    while num1 > 0 or num2 > 0:
        digit1 = num1 % 10
        digit2 = num2 % 10
        sum_digits = (digit1 + digit2) % 10
        result += sum_digits * multiplier
        num1 //= 10
        num2 //= 10
        multiplier *= 10
    
    return result

def last_survivor(letters, coords): 
    str_list = list(letters)
    for index in coords:
        del str_list[index]
    return str_list[0]

def initialize_names(name):
    parts = name.split()
    if len(parts) <= 2:
        return name
    
    first_name = parts[0]
    last_name = parts[-1]
    middle_initials = ' '.join(f"{name[0]}." for name in parts[1:-1])
    
    return f"{first_name} {middle_initials} {last_name}"


def get_issuer(number):
    number = str(number)
    
    if len(number) == 15 and (number.startswith('34') or number.startswith('37')):
        return 'AMEX'
    elif len(number) == 16 and number.startswith('6011'):
        return 'Discover'
    elif len(number) == 16 and number.startswith(('51', '52', '53', '54', '55')):
        return 'Mastercard'
    elif len(number) in (13, 16) and number.startswith('4'):
        return 'VISA'
    else:
        return 'Unknown'
    


def even_or_odd(s):
    even_sum = 0
    odd_sum = 0
    
    for char in s:
        digit = int(char)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    
    if even_sum > odd_sum:
        return "Even is greater than Odd"
    elif odd_sum > even_sum:
        return "Odd is greater than Even"
    else:
        return "Even and Odd are the same"