new_list = []
sum1 = 0


for i in range(1,10): 
    sum1 = sum1 + i
    new_list.append(i)
print(sum1)
print(new_list)
print(len(new_list))

new_list = []
num1 = int(input("please enter first number:"))
num2 = int(input("please enter second number:"))
sum2 = 0
for i in range(num1,num2):
    sum2 = sum2 + i 
    new_list.append(i)

print(sum2)
print(new_list)

new_list = []
num1 = int(input("please enter first number:"))
num2 = int(input("please enter second number:"))
sum3 = 0
for i in range(num1,num2):
    sum3 = sum3 + i 
    new_list.append(i)
print(max(new_list))
print(min(new_list))
print(sum(new_list))



num1 = int(input("How many numbers do you want to enter?"))
new_list = []
sum4 = 0
for i in range(num1):
    new_list.append(i)
    sum4 = sum4 + i
print(new_list)
print(sum4)


cars = [
    "Toyota",
    "Honda",
    "Ford",
    "Chevrolet",
    "BMW"
]
first_three = cars[:3]
last_two = cars[-2:]
print(first_three)
print(last_two)
print(cars[-3])
print(cars[-4])

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


