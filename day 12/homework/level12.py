day = int(input("please enter number:"))


if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 2:
    print("Thursday")
elif day == 2:
    print("Friday")
elif day == 2:
    print("Saturday")
elif day == 2:
    print("Sunday")
else:
    print("Error")

i = 0

while i <= 10:
    if i % 2 == 0:
        print(str(i) + " is even")
    else:
        print(str(i) + " is odd")
    i = i + 1

age = int(input("please enter your age:"))
if age >= 18:
   print("You can vote")
else:
   print("You cant vote")



budget = int(input("Please enter your budget:"))
if budget == 150:
    print("you can buy wallet")
else:
    print("you cant buy")


num1 = float(input("Please enter first number:"))
num2 = float(input("Please enter second number:"))
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
operation = int(input("enter opereiton:"))

if operation == 1:
   print(num1 + num2)
elif operation == 2:
   print(num1 - num2)
elif operation == 3:
   print(num1 * num2)
elif operation == 4:
   print(num1 / num2)

total = 0
number = 1

while number <= 100:
    total += number
    number += 1

print("ყველა რიცხვის ჯამი 1-დან 100-მდე არის:", total)