favorite_cars = []
for i in range(5):
   car_name = input("please enter your favorite car name: ")
   favorite_cars.append(car_name)

print("your favorite cars are: ")
print(favorite_cars)


favorite_movies = ["Logan", "Titanic", "Forrest Gump"]
Best_movie = favorite_movies[1]
print(Best_movie)

random_information = ["BMW", "pagani", True, 10]
random_information[0] = 16

favorite_fruits = ["Apples", "Bananas", "Oranges", "Mango", "Strawberries"]
new_fruit = "Dragon Fruit"
favorite_fruits.append(new_fruit)
favorite_fruits.remove("Bananas")
print(favorite_fruits)

#sum ფუნქციის კლონი
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

sum = 0
 
for number in numbers:
     sum = sum + number
    
print(sum)

#max ფუნქციის კლონი 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

max_num = numbers[0]
for number in numbers:
    if max_num < number:
        max_num = number

print(max_num)


#min ფუნქციის კლონი 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

min_num = numbers[0]
for number in numbers:
    if max_num > number:
        min_num = number

print(min_num)

names = []
for i in range(5):
    name = input("Please enter name: ")
    names.append(name)

# შევამოწმოთ რამდენჯერ მიერ არჩეული სახელი გამოიტანება სიაში
selected_name = input("enter name: ")
count = names.count(selected_name)

print(count)



numbers = [1, 2, 3, 4, 5]
numbers.pop(0)
numbers.pop(4)
print(numbers)























