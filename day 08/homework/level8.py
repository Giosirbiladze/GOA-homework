

# print(True and True) # True
# print(True and False) # False
# print(False and True) # False
# print(False and False) # False 

# print(True or True) # True
# print(True or False) # True
# print(False or True) # True
# print(False or False) # False


num=27
print("----------- AND -----------")

print(num >= 1 and num <= 10) 
print(num >= 1 and num <= 4) 
print(num > 5 and num <= 10) 
print(num > 5 and num > 10) 
print(num == 1 and num != 2)
print("----------- OR -----------")

print(num >= 1 or num <= 10) 
print(num >= 1 or num <= 4) 
print(num > 5 or num <= 10) 
print(num > 5 or num > 10) 
print(num == 1 or num != 10)

num1 = float(input("please enter first number: "))
num2 = float(input("please enter second number: "))
num3 = float(input("please enter third number: "))
num4 = float(input("please enter fourth number: "))
num5 = float(input("please enter fifth number: "))

print(num1 + num2)
print(num3 - num4)
print(num5 / num1)
print(num3 * num5)
print(num4 // num2)
print(num1 % num2)

your_age = int(input("please enter your age: "))
print(your_age > 18 and your_age < 20)

A = 10
B = 10.0 
print(type(A))
print(type(B))
#A-ის ტიპი არის integer ანუ მთელი რიცხვი
#B-ის ტიპი არის float ანუ ათწილადი

num6 = 11
num7 = 11.0
num8 = "11"
C = False 
print(type(num6))
print(type(num7))
print(type(num8))
print(type(C))