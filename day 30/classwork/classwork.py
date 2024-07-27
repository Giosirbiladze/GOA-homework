def filter_odd(numbers):
    return [num for num in numbers if num % 2 == 0]

print(filter_odd([1, 2, 3, 4, 5, 6]))

def even_sum(numbers):
    sum_even = 0
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
    return sum_even


print(even_sum([1, 2, 3, 4, 5, 6]))  

def odd_index_sum(numbers):
    sum_odd_indices = 0
    for index in range(len(numbers)):
        if index % 2 == 1:  
            sum_odd_indices += numbers[index]
    return sum_odd_indices

print(odd_index_sum([1, 2, 3, 4, 5, 6]))