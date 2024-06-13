# 1) პირველ რიგში შემოგვაქვს ცვლადი password
# 2) შემდეგ input ის დახმარეთ მომხმარებელს შეყავს პაროლი
# 3) კოდი if და else ის გამოყენებით თუ შემოტანილი პაროლი სწორია ეკრანზე გამოვა მესიჯი: პაროლი სწორია თუ პაროლი არასწორია: პაროლი არასწორია



password = input("please enter password:" )

if password == "luka1234":
   print("password is correct")
else: 
    print("password is incorrect")


    

product = 1


for i in range(5):
    num = int(input("Please enter number: "))
    product = product * num

print(product)

Num1=0

for num in range(5,16):
    Num1 = Num1 + num
print(Num1)