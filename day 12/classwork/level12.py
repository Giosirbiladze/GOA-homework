i = 20
while i >= 1:
    print(i)
    i = i - 1

i = 0
while i <= 10:
    print(i)
    i = i + 2

i = 1
sum = 0


while i <= 10:
    sum = sum + i
    i = i + 1
    # while ციკლი არის საკონტროლო ნაკადის განცხადება, რომელიც საშუალებას აძლევს კოდის განმეორებით შესრულებას, იმისდა მიხედვით, დაკმაყოფილებულია თუ არა პირობა.

correct_password = "gio"
input_password = ""
while correct_password != input_password:
    input_password = input("Please enter correct password:")
    if correct_password == input_password:
       print("password is correct")
    else: print("password is incorrect")

i = 1
while i <= 9:
    print(i)
    i = i + 2

correct_age = 18
input_age = int()

while input_age < correct_age:
    input_age = int(input("please enter your age:"))
    if input_age == correct_age:
        print("you can login")
    else: print("you cant login")


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