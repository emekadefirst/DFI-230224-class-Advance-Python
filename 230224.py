import random as r
1
def usr_acc_num():
    random_integers = ''.join(str(r.randint(0, 9)) for _ in range(10))
    return random_integers

print("Welcome, what would you like to do? ")
print("1. Open account\n2. Transfer\n3. Airtime\n4. Internet\n5. Balance\n6. Bills & Utitilies")

res = str(input())
#assigment
if res == "1": 
    firstname = str(input("Your firstname\n>> ")).upper()
    surname = str(input("Your lastname\n>> ")).upper()
    other_name = str(input("Your other name\n>> ")).upper()
    email = str(input("Your email\n>> ")).upper()
    number = int(input("Your Phone number\n>> "))
    address = str(input("your address\n>> ")).upper()
    dob = str(input("Yojur date of birth\n>> "))
    account_number = usr_acc_num()
    print(f"Dear {firstname} {surname} {other_name}, your account was successfully created,\nyour account number is {account_number}\nThanks for joining the family")
