name_list = [
  "mate",
  "dato",
  "gio",
  "lasha",
  "vaxo",
  "gio"

]
for i in name_list:
    if i == "gio":
        print("hello admin")
    else:
        print("hello user")

cars = [
    "Toyota", 
    "Honda", 
    "Ford", 
    "Chevrolet", 
    "BMW"

    ]


first_three = []
for i in range(min(3, len(cars))):
    first_three.append(cars[i])


last_two = []
for i in range(max(0, len(cars) - 2), len(cars)):
    last_two.append(cars[i])
print(first_three)
print(last_two)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0

for num in numbers: 
    if num % 2 == 0:
        even_sum += num

print("Sum of even numbers:", even_sum)
