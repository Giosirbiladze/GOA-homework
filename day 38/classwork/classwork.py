def is_divisible(n,x,y):
    return n%x == 0 and n%y == 0

def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)


def feast(beast, dish):
  beast_first_and_last = beast[0] + beast[-1]
  dish_first_and_last = dish[0] + dish[-1]
  return beast_first_and_last == dish_first_and_last 


def say_hello(name, city, state):
    name1 = ""
    for i in name:
        name1 += i + " "
    name1 = name1[:-1]
    return f"Hello, {name1}! Welcome to {city}, {state}!"


def points(games):
    score=0
    for i in games:
        i= i.split(":")
        if i[0] > i[1]:
            score += 3
        elif i[0] == i[1]:
            score += 1
    return score