num1 = 25
num2 = 7
print(num1+num2)
print(num1-num2)
print(num1/num2)
print(num1//num2)
print(num1%num2)
print(num1**num2)

balance = 1000
balance += 250
print(balance)
balance -= 100
print(balance)
balance *= 2
print(balance)
balance /= 4
print(balance)


price = int(input("Enter price: "))
discount = float(input("Enter discount: "))
print(price - discount)


INTEREST = 1.18
nis = int(input("Enter sum mony: "))
print(nis * INTEREST)


first_name = "David"
last_name = "Cohen"
city = "Tel Aviv"
print(f"Hello, my name is {first_name} {last_name} and I live in {city}.")
print("Hello, my name is " + first_name +" "+ last_name + " and I live in " + city)

name = input("Enter your name: ")
print(len(name))
print(name.upper())
print(name.lower())


sentence = input("Enter sentence: ")
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.title())

sentence = input("Enter sentence: ")
new_sentence = sentence.strip()
print(sentence)
print(new_sentence)
print(len(sentence))
print(len(new_sentence))

sentence = "I love Java programming"
txt = sentence.replace("Java", "python")
print(txt)
print(sentence.count("love"))
print(sentence.startswith("I"))
print(sentence.endswith("programming"))

word = "Programming"
print(word[0])
print(word[-1])
print(word[5:])



a = "100"
b = "25"
c = 10
d = 5.5
a = int(a)
b = float(b)
c = str(c)
d = round(d)
print(type(a), type(b) ,type(c) , type(d)) 


age = int(input("Enter your age: "))
print(age + 10)


TAX = 1.18
price = int(input("Enter Price: "))
print(price * TAX)

first_name = input("first name: ")
last_name = input("last name: ")
age = int(input("Age: "))
wage = int(input("wage: "))
seniority = int(input("seniority: "))
print(f"""
=== Emploee ===
Name: {first_name}
Last name: {last_name}
Annual Salary: {wage * 12}
With 5 percent: {(wage * 12) * 1.05}
{len(first_name)}
""")


usd_rate = 3.25
val= int(input("val: "))
print(val/usd_rate)
print(val/3.75)
print((val/usd_rate) * 1.02)


first_name = input("firs name: ").lower()
last_name = input("last name: ").lower()
year = input("Year: ").lower()
email = f"{first_name}.{last_name}.{year}@gmail.com"
print(email)

sentence = input("Enter sentence: ")
print(sentence)
print(len(sentence))
print(sentence.upper())
print(sentence.lower())
print(sentence.count("a"))
txt = sentence.replace(" ", "_")
print(txt)

client = input("client: ")
product = input("product: ")
price = float(input("Price: "))
quantity = int(input("quantity: "))
discount = float(input("discount: "))
vat = float(input("vat: "))


subtotal = price * quantity
after_discount = subtotal - discount
vat_amount = after_discount * (vat /100)
total = after_discount + vat_amount

print(f"""
================================
          PURCHASE INVOICE
================================

Customer: {client}
Product: {product}

Unit Price: {price:.2f}
Quantity: {quantity:.2f}

Subtotal: {subtotal:.2f}
Discount: {discount:.2f}
After Discount: {after_discount:.2f}

VAT: {vat}%
VAT Amount: {vat_amount:.2f}

TOTAL: {total:.2f}

================================
       THANK YOU FOR SHOPPING
================================

""")