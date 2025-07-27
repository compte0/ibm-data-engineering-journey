'''IF'''
user_choice = "Withdraw Cash"
if user_choice == "Withdraw Cash":
   amount = int(input("Enter the amount to withdraw: "))
   if amount % 10 == 0:
       print("Amount dispensed: ", amount)
   else:
       print("Please enter a multiple of 10.")
else:
   print("Thank you for using the ATM.")

'''For 1'''
#création de la liste
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

#boucle de défilement des couleurs
for color in colors:
   print(color)

'''For 2'''
for number in range(1, 10):
   print(number);

'''For 3'''
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
   print(f"At position {index}, I found a {fruit}")


'''While'''
count = 1
while count <= 10:
   print(count)
   count += 1
