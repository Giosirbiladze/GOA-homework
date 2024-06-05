your_age = int(input("please enter your age: "))
print(your_age > 18 and your_age <= 25)

your_budget = int(input("please enter your budget: "))
print(your_budget > 50 or your_budget > 100)

your_age = int(input("please enter your age: "))
your_budget = int(input("please enter your budget: "))
if your_age > 18 and your_budget > 75: 
     print("you can buy this product")
else: 
    print("you cant buy this product")