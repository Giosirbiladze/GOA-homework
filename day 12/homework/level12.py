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