numbers = 10,20,30,40,50
print(numbers)
print(numbers[0])
print(len(numbers))
print(numbers[2])


students = "Noa", "Itay", "Maya", "Daniel", "Tamar", "Omer", "Shira"
for name in students:
    print(name)
print("Noa" in students)
print(len(students))



nums = 1,2,3,4,5,6,7
print(nums[:3])
print(nums[3:])
print(nums[::-1])




item = "Pen", 14.0, 23, "writing"
print(item[0])
print(item[1])
print(item[2])
print(item[3])



nums = 1,2,3,4,5,6,7,8,9,10
total = 0
max_num = float('-inf')
evens = 0
for n in nums:
    total += n
    if n > max_num:
        max_num = n
    if n % 2 == 0:
        evens += 1
print(f"Total: {total}, Max: {max_num}, Evens: {evens}")





products = ("Laptop", "Mouse", "Keyboard", "Screen", "Printer")
three = products[:3]
last_tow = products[2:]
new = three + last_tow
print(new)




# Dictonaries

student = {"name": "David", "age": 22, "grade": 95, "city": "Tel Aviv"}
print(student["name"])
print(student["age"])
print(student["grade"])
print(student["city"])




car = {"brand":"TESLA", "model":"Y", "year":1950, "price":100000}
car["price"] = 200000
car["year"] = 1940
car["coclor"] = "Red"
print(car)



salaries = {"David": 12000, "Moshe": 15000, "Dana": 13500}
for k,v in salaries.items():
    print(f"{k}: {v}")
salaries["David"] = 13000
salaries["Moty"] = 17000
for k,v in salaries.items():
    print(f"{k}: {v}")



products = {"Laptop": 1200, "Smartphone": 800, "Headphones": 150, "Keyboard": 75, "Mouse": 40, "Monitor": 300, "Webcam": 85}
search = input("Enter a product: ")
if search in products:
    print(products[search])
else:
    print("Product not found!")



students = {"Alice": 95, "Bob": 82, "Charlie": 78, "Diana": 91, "Ethan": 88}
for k ,v in students.items():
    print(f"Studrnt: {k} | Grade: {v}")


grades = {"David": 90, "Moshe": 75, "Dana": 100, "Noa": 55, "Avi": 82}
total = 0
max_g = float('-inf')
max_n = None
failed = 0
for k,v in grades.items():
    if v > 80:
        print(f"{k}: {v}")
    if v > max_g:
        max_g = v
        max_n = k
    if v < 60:
        failed += 1
    total += v
print(total/len(grades))
print(f"{max_n}")
print(failed)





products = {"Laptop": 1200, "Smartphone": 800, "Headphones": 150, "Keyboard": 75, "Mouse": 40, "Monitor": 300, "Webcam": 85}
search = input("Enter a product: ")
if search in products:
    change = int(input("Enter Price: "))
    products[search] = change
else:
    product = input("Enter a product: ")
    price = int(input("Enter Price: "))
    products[product] = price
print(products)



students = [{"name": "David", "age": 20, "grade": 90}, {"name": "Moshe", "age": 22, "grade": 75}, {"name": "Dana", "age": 21, "grade": 100}, {"name": "Noa", "age": 19, "grade": 55}, {"name": "Avi", "age": 23, "grade": 82}]
for student in students:
    print(student["name"])
for student in students:
    print(student["grade"])
for student in students:
    if student["grade"] > 80:
        print(student["name"])
average = sum(student["grade"] for student in students) / len(students)
print(average)
max_n = None
max_s = float('-inf')
for student in students:
    if student["grade"] > max_s:
        max_s = student["grade"]
        max_n = student["name"]
print(f"{max_n}: {max_s}")
print("\n\n")

new_student = {"name": input("Enter name: "), "age": int(input("Enter age: ")), "grade": int(input("Enter grade: "))}
students.append(new_student)
print(students)

name = input("Enter name: ")
grade = int(input("Enter score: "))
for student in students:
    if student["name"] == name:
        student["grade"] = grade


name = input("Enter name: ")
for student in students:
    if student["name"] == name:
        students.remove(student)

print(students)



classroom = {"Class A": ["David", "Moshe", "Dana"], "Class B": ["Noa", "Avi", "Michael"], "Class C": ["Daniel", "Shir", "Yossi"]}
for c in classroom:
    print(c)
print(classroom["Class A"])

name = input("Enter Name: ")
classroom["Class B"].append(name)
print(classroom["Class B"])
name = input("Enter Name: ")
if name in classroom["Class C"]:
    classroom["Class C"].remove(name)
print(f"Class A: {len(classroom['Class A'])} | Class B: {len(classroom['Class B'])} | Class C: {len(classroom['Class C'])}")





products = {
    "Laptop":   {"price": 4500,  "stock": 10},
    "Mouse":    {"price": 80,    "stock": 50},
    "Keyboard": {"price": 150,   "stock": 20}
    }

for k,v in products.items():
    print(f"{k}: {v["price"]}")
for k,v in products.items():
    print(f"{k}: {v["stock"]}")
add_qua = int(input("Enter add: "))
products["Laptop"]["stock"] += add_qua
new_product = input("Enter product: ")
products[new_product] = {"price":int(input("Enter price: ")), "stock":int(input("Enter quantity: "))}

for k,v in products.items():
    if v["price"] > 100:
        print(k)




employees = [
    ("David", "Development", 15000),
    ("Moshe", "Marketing",   12000),
    ("Dana",  "Development", 18000),
    ("Noa",   "HR",          11000)
            ]

for e in employees:
    print(e[0])
max_s = float('-inf')
emploee = None
total = 0
for e in employees:
    name, platoon, salary = e
    if platoon == "Development":
        print(e)
    if salary > max_s:
        max_s = salary
        emploee = e
    total += salary
print(emploee)
print(total/len(employees))



inventory = {
    "Laptop": 10,
    "Mouse": 50,
    "Keyboard": 20
    }
pro = input("Enter Product: ")
if pro in inventory:
    qua = int(input("Enter Quantity: "))
    if qua <= inventory[pro]:
        inventory[pro] -= qua
        print(inventory)
    else:
        print("not enough quantity!")
else:
    print("The product Not found!")


votes = {
    "David": 0,
    "Moshe": 0,
    "Dana": 0
    }
while True:
    val = input("Enter a name to add a vote, or 'stop' to exit: ")
    if val in votes:
        votes[val] += 1
        print(votes)
    elif val == "stop":
        break
print(max(votes, key=votes.get))





contacts = {
    "David": "050-1234567",
    "Dana": "052-7654321",
    "Moshe": "054-9876543"
}

while True:
    val = input("""
1. Add a contact
2. Search for a contact
3. Update a phone number
4. Delete a contact
5. Display all contacts
0. Exit
your choice: """)
    if val == "1":
        new_name = input("Enter New name: ")
        contacts[new_name] = input("Enter phon number: ")
    elif val == "2":
        name = input("Enter Name: ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Name not found!")
    elif val == "3":
        name = input("Enter Name: ")
        if name in contacts:
            contacts[name] = input("Enter phon number: ")
        else:
            print("Name not found!")
    elif val == "4":
        name = input("Enter Name: ")
        if name in contacts:
            del contacts[name]
    elif val == "5":
        print(contacts)
    elif val == "0":
        break



products = [
    {"name": "Laptop", "price": 4500, "stock": 10},
    {"name": "Mouse", "price": 80, "stock": 50},
    {"name": "Keyboard", "price": 150, "stock": 20},    {"name": "Screen", "price": 900, "stock": 15}
    ]

while True:
    val = input("""
===== Store Management =====

1. Show all products
2. Add product
3. Search product
4. Update product price
5. Update product stock
6. Sell product
7. Show products by price
8. Show products with low stock
9. Show total inventory value
0. Exit
your choice: """)
    if val == "1":
        print(products)
    elif val == "2":
        products.append({"name":input("Enter New item: "), "price":int(input("Enter price: ")), "stock": int(input("Enter stock: "))})
    elif val == "3":
        name = input("Enter name: ")
        for pro in products:
            if pro["name"] == name:
                print(pro)

    elif val == "4":
        name = input("Enter name: ")
        for pro in products:
            if pro["name"] == name:
                pro["price"] = int(input("Enter price: "))

    elif val == "5":
        name = input("Enter name: ")
        for pro in products:
            if pro["name"] == name:
                pro["stock"] = int(input("Enter Quantity: ")) 
    elif val == "6":
        name = input("Enter name: ")
        for pro in products:
            if pro["name"] == name:
                qua = int(input("Enter quantity: "))
                if pro["stock"] >= qua:
                    pro["stock"] -= qua
                else:
                    print("Not enough stock")
    elif val == "7":
        price = int(input("Enter price: "))
        high_from_price = [pro for pro in products if pro["price"] > price]
        print(high_from_price)
    elif val == "8":
        for pro in products:
            if pro["stock"] < 10:
                print(pro)
    elif val == "9":
        total = 0
        for pro in products:
            total += (pro["price"] * pro["stock"])
    elif val == "0":
        break