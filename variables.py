first_name = "David"
last_name = "Cohen"
age = 25
city = "Tel Aviv"
email = "david@gmail.com"

print(f"===== User Details =====\nFirst Name: {first_name}\nLast Name: {last_name}\nAge: {age}\nCity: {city}\nEmail: {email}\n========================")

birth_year = 2001
current_year = 2026
print(f"You are approximately {current_year - birth_year} years old.")


width = 12
height = 13
print(f"Surface: {width * height}.")
print(f"Scop: {2*width + 2*height}.")


name = "David"
age = 25
height = 1.78
is_student = True
salary = 8500
print(f"{name}: {type(name)}\n{age}: {type(age)}\n{height}: {type(height)}\n{is_student}: {type(is_student)}\n{salary}: {type(salary)}")


first_name = input("Enter your name: ")
last_name = input("Enter your last name: ")
city = input("Enter your city: ")
age = input("Enter your age: ")
print(f"====== Welcome =======\n{first_name}\n{last_name}\n{city}\n{age}\n======================")



num1= int(input("Enter a only nujmber (1):"))
num2= int(input("Enter a only nujmber (2):"))

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)



product = input("Enter Product: ")
price = int(input("Enter Price: "))
quantity = int(input("Enter Quantity: "))
print(f"""====== Purchase Receipt ======
Product: {product}
Price: {price}
Quantity: {quantity}
Total: {price * quantity}
==============================""")



emploee = input("Enter nemploee's name: ")
hours = int(input("Enter hours for month: "))
per_hour = int(input("Enter how meny: "))
print(f"""===== Total for a month =====
Emploee: {emploee}
Hours: {hours}
Per hour: {per_hour}
subtotal: {hours * per_hour}""")


sum = int(input("Enter sum of price: "))
tip = int(input("Enter TIP: "))
guests = int(input("Enter Guests: "))
print(f"""
{tip}
{sum+tip}
{(sum+tip)/guests}""")


a = 10
b = 20
c = a
a = b
b = c
print(a)
print(b)


first_name = input("First Name: ")
last_name = input("Last Name: ")
age = int(input("Age: "))
univercity = input("Univercity: ")
name_of_course = input("Name of course: ")
sum_of_month = int(input("Number of months in the course: "))
price_for_month = int(input("Price for Month: "))
print(f"""================================
       STUDENT REGISTRATION
================================

Student: {first_name}
Age: {age}
Institution: {univercity}
Course: {name_of_course}
Duration: {sum_of_month} Months
Monthly Price: {price_for_month}

Total Course Price: {price_for_month * sum_of_month}

================================
Registration completed!
================================
""")


