age = int(input("Enter your age: "))
print("Adult" if age >= 18 else "Minor")


number = int(input("Enter number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")



number = int(input("Enter number: "))
print("Even" if number % 2 == 0 else "Add")

num1 = int(input("Enter 1 number: "))
num2 = int(input("ENter 2 number: "))
if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)
else:
    print(f"{num1} = {num2}")



password = "Python123"
try_password = input("Enter Password: ")
if try_password == password:
    print("Access")
else:
    print("Denied")


number = int(input("Enter number: "))
if 10 >= number > 1:
    print("Between 1-10")
elif 50 >= number >= 11:
    print("Between 11-50")
elif 100 >= number >= 50:
    print("Between 50-100")
else:
    print("Out of the🎯...")




Grade = int(input("Enter graed: "))
if 90 <= Grade <= 100:
    print("Exellent")
elif 89 <= Grade <= 80:
    print("Very Good!")
elif 79 <= Grade <= 70:
    print("Good")
elif 69 <= Grade <= 60:
    print("Passed")
elif 59 <= Grade <= 0:
    print("Failed")
else:
    print("Invalid Grade")




correct_username = "admin"
correct_password = "123456"
user = input("User: ")
password = input("Password: ")

if correct_username == user and correct_password == password:
    print("Login Successfuf")
elif correct_username == user and correct_password != password:
    print("Wrong Password")
elif correct_username != user:
    print("Unknown User")



age = int(input("Enter age: "))
price = int(input("Enter Price: "))
if age >= 60:
    print(price * 0.80)
elif age < 18:
    print(price * 0.90)
else:
    print(price)


num = int(input("Enter number: "))
if num % 3 == 0:
    print("%3 == 0")
if num %5 == 0:
    print("%5==0")
if num %5 == 0 and num %3 == 0:
    print("% 5&3 == 0")
else:
    print("Not")


age = int(input("Enteer Age: "))
if age < 18:
    with_adult = input("Press 1 if you with adult: ")
print(age >= 18 or age < 18 and with_adult == "1")



grades = float(input("Enter grades: "))
if 85 <= grades <= 90:
    income = int(input("Enter income: "))
print(grades > 90 or 85 <= grades <= 90 and income < 5000)



correct_username = "admin"
correct_password = "123456"
user = input("User Name: ")
password = input("Password: ")
is_active = input("Press 1 if Active: ")
print(user == correct_username and password == correct_password and is_active == "1")


num = int(input("Enter number:"))
if num >= 20 and num <=80:
    print("20-80")
if not (num <=80) or not(20 <= num):
    print("Not 20-80")


balance = 5000
atm = float(input("Enter ATM: "))
if atm > 0:
    if balance > atm:
        balance-=atm
        print(balance)
    else:
        print("Not enough money")
else:
    print("Negative ATM")

client = float(input("Enter Age: "))
club = input("Press 1 If a club member: ")
if club == "1":
    discount = 0.90
else:
    discount = 1.00
if 0 < client < 12:
    price = 25
elif client < 18:
    price = 35
else:
    price = 50
print(price * discount)


age = float(input("Enter Age: "))
if age > 21:
    salary = float(input("Enter salary: "))
    if salary > 7000:
        seniority  = float(input("Enter Seniority: "))
        if seniority > 12:
           print("Loan successful!!")
        else:
           print("Seniority Less than a year")
    else:
        print("Not enough Salary")
else:
    print("The Age lass than 21")



val = input("""1. Motorcycle
2. Car
3. Commercial vehicle
Select vehicle type: """)
if val == "1":
    price = 10.0/60
elif val == "2":
    price = 20.0/60
elif val == "3":
    price = 30.0/60
time = float(input("Enter time: "))
if time < 60.00:
    discount = 0.90
elif time > 300.00:
    discount = 0.85
else:
    discount = 1.00
print((price * time) * discount)


num1 = int(input("Enter 1 number: "))
num2  = int(input("Enter 2 number: "))
act = input("""
1. +
2. -
3. *
4. /
Press Action: """)
if act == "1":
    print(num1+num2)
elif act == "2":
    print(num1-num2)
elif act == "3":
    print(num1 * num2)
elif act == "4":
    if num2 < 0:
        print(num1/num2)
    else:
        print("Cannot / in zero")
else:
    print("Error Invalid choice!")



year = int(input("Enter year: "))
if year % 400 == 0 or year %4 == 0 and year %100 != 0:
    print("leap year")
elif year %100 == 0 and year % 400 != 0:
    print("Not leap year")
else:
    print("Not leap year")


base = 50
hours = int(input("Enter Hours: "))
if hours <= 182:
    print(base * hours)
elif hours > 182:
    extension_hours = hours - 182
    if extension_hours > 2:
        print(
            (base * hours)
             + (2 * (base*0.25))
             + ((extension_hours-2) * (base*0.50))
            )
    else:
        print((base*hours) + ((extension_hours) * (base*0.25)))


age = int(input("Enter age: "))
price = float(input("Enter Price: "))
is_in_club = input("Press 1 if in club: ")
is_open = input("Press 1 if it's opened: ")
has_invoice = input("Press 1 if has invoice: ")
sum_of_days = int(input("Enter days: "))

if has_invoice == "1":
    if is_open != "1":
        if price > 0:
            if is_in_club == "1":
                print(True, price)
            elif not(is_in_club == "1") and sum_of_days < 14:
                print(True, price)
            else:
                print(False, "the client not in the club and 14 days have passed")
        else:
            print("the price is Negative")
    else:
        print("The product it's opened")
else:
    print("No invoice!")
        
