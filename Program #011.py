                                # My Program
                                 
                                #  Food App

food = input("Enter the name of the Food : Biryani , Qurma , Pasta , Labishiri ")
drink = input("Enter the name of the Drink :  Labishiri ")

bill = 0

if food == "Biryani" or "biryani" :
    bill +=12
if food == "Qurma" or "qurma" :
    bill +=11
if food == "Pasta" or "pasta" :
    bill +=10
if food == "Biryani" or "biryani" or  "Qurma" or "qurma" "Pasta" or "pasta" :
    if drink == "Labishiri" or "labishiri":
        bill += 20

print(f"Your total bill is {bill}$")