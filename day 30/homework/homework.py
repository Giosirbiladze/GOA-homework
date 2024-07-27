def odd_index_sum(numbers):
    sum_odd_indices = 0
    for index in range(len(numbers)):
        if index % 2 == 1:  
            sum_odd_indices += numbers[index]
    return sum_odd_indices


print(odd_index_sum([1, 2, 3, 4, 5, 6]))