def filter_list(l):
    return [item for item in l if isinstance(item, int) and item >= 0]


def sum_two_smallest_numbers(numbers):
    numbers_sorted = sorted(numbers)
    return numbers_sorted[0] + numbers_sorted[1]


def solution(text, ending):
    return text.endswith(ending)

def stray(arr):
    unique_elements = set(arr)
    for element in unique_elements:
        if arr.count(element) == 1:
            return element
        
def sort_by_length(arr):
    return sorted(arr, key=len)