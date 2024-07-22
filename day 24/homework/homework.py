# code wars 1

def make_upper_case(s):
    return s.upper()

#code wars 2

def hero(bullets, dragons):
    return dragons * 2 <= bullets

#code wars 3 

def invert(lst):
    new_list = []
    for i in lst:
        new_list.append(-i)
    return new_list

#code wars 4 

def difference_in_ages(ages):
    max_age = ages[0]
    min_age = ages[0]
    for i in ages:
        if max_age < i:
            max_age = i
        elif min_age > i:
            min_age = i
    difference = max_age - min_age
    return(min_age, max_age, difference)
          