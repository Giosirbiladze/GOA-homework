num = 0
for i in range (0,100):
    num = num + i
print(num)

num = 0
for i in range (0,100):
    num = num * i
print(num)

num = 0
for i in range (0,100):
    num = num - i
print(num)

num = 0
for i in range (1,100):
    num = num / i
print(num)

sum = 0
num = int(input("please enter number:"))
for i in range (0,num):
    sum += i
print(sum)

sum_number = 0
multiply = 1

num1 = int(input("please enter first number:"))
num2 = int(input("please enter second number:"))
for i in range (num1,num2):
    sum_number += i
    multiply *= i
print(sum_number,multiply)

   