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


def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


choice = input("Enter choice (1/2/3/4): ")


if choice in ('1', '2', '3', '4'):
    # Input two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input")


total = 0
number = 1

while number <= 100:
    total += number
    number += 1

print("ყველა რიცხვის ჯამი 1-დან 100-მდე არის:", total)