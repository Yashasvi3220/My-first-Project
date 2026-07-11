# ATM WITHDRAWALS SYSTEM

print("-"*25)
print("   SAFE ATM SYSTEM  ")
print("-"*25 +"\n")

Balance = 100000
print(f"Balance : {Balance}")
pin= int(input("Please inter the pin : "))
if pin==123456:
 
 try:
    User_amount = int(input("Enter your amount :"))
    remaining_amount= Balance - User_amount
    if User_amount <0:  
        print("Invalid amount")
    elif User_amount> Balance:
        print("Not saficient balance"+ "\n")
    else:
        print(f"Transiction is successful remaing amount is :{remaining_amount}")


 except ValueError:
    print("Transiction is unsuccessful.please try again")


else:
   print("Wrong pin,please try again ")

print("Thanks for visiting")

print("_"*25)
 
