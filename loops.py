count = 1
while count < 11:
    print(count) 
    count += 1


count = 10
while count >= 1:
    print(count)
    count -= 1
print("START!")


count = 1
while count <= 50:
    if count % 2 == 0:
        print(count)
    count += 1


num = int(input("Enter a number: "))
for i in range(1,6):
    print(i * num)


count = 0
for i in range(1, 101):
    count += i
print(count)


password = "Python123"
while True:
    val = input("Enter Password: ")
    if val == password:
        print("Welcome!")
        break
    else:
        continue




secret_number = 27
while True:
    val = int(input("Enter Password: "))
    if val == secret_number:
        print("Good!")
        break
    else:
        continue

count = 0
while True:
    val = int(input("Ente ra number: "))
    if val == 0:
        break
    count += val
print(count)


grades = []
while True:
    val = int(input("Ente ra grade: "))
    if val == 999:
        break
    grades.append(val)
print(len(grades))
print(sum(grades))
print(sum(grades)/len(grades))


total = 0
count = 0
while True:
    val = int(input("Ente ra number: "))
    if val < 0:
        break
    count += 1
    total += val
print(total)
print(count)



num = int(input("Enter a number: "))
i = 1
while i < 11:
    print(i * num)
    i += 1


num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num//10
    count += 1
print(count)


  

new = 0
num = int(input("Enter a number: "))
while num > 0:
    s = num % 10
    num = num // 10
    new = (new * 10) + s
print(new)


number = int(input("Enter a number: "))
count = 2
flag = True
while count != number:
    if number % count == 0:
        flag = False
        break
    count += 1
print(flag)



balance = 5000
while True:
    val = input("""
1. Check balance.
2. Deposit money.
3. Withdraw money.
4. Log out.
Enter your choice: """)

    if val == "1":
        print(balance)
        continue
    elif val == "2":
        amount = int(input("Add amount: "))
        if amount > 0:
            balance += amount
            continue
        else:
            print("The amount cannot be negative")
            continue
    elif val == "3":
        amount = int(input("Withdrawal of an amount: "))
        if amount > 0:
            if balance >= amount:
                balance -= amount
                continue
            else:
                print("not enough money!")
                continue
        else:
            print("The amount must be positive!")
            continue
    elif val == "4":
        print("good Bay")
        break
    else:
        continue

count = 1
while True:
    if count == 15:
        break
    print(count)
    count += 1
    


count = 1
while count < 31:
    if count % 3 == 0:
        count += 1
        continue
    print(count)
    count += 1


while True:
    x = int(input("Enter a number: "))
    if x == 100:
        print("💐")
        break


for i in range(1,21):
    print(i)


for i in range(0,101,5):
    print(i)

total = 0 
for i in range(1, 101):
    total += i
print(total)



num  = int(input("Enter a number: "))
for i in range(1,11):
    print(i * num)


start= int(input("Enter Start: "))
end = int(input("Enter End: "))
total = 0
for i in range(start, end+1):
    total += i
print(total)


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


columns = int(input("Enter Columns: "))
rows = int(input("Enter Rows: "))
for i in range(rows):
    for j in range(columns):
        print(f"*" , end=" ")
    print()


for i in range(1,7):
    for j in range(i):
        print("*", end="")
    print()


for i in range(1,11):
    for j in range(1,11):
        print(f"{i*j:4}" , end= "")
    print()


for i in range(1,6):
    for j in range(1, i +1):
        print(j,i)




while True:
    count = 0
    val = input("""
===== MATH GAME =====

1. Start Game
2. View Instructions
3. Exit

Choose: """)
    if val == "1":
        for i in range(1,11):
            print( f"question {i}")
            answer = input(f"answer: {i} * {i} - 2: ")
            if (i * i) -2 == int(answer):
                count += 1
        print(count)
    elif val == "2":
        print("""
התוכנית תציג סדרה של 10 תרגילים חשבוניים.
בכל תרגיל המשתמש יכניס תשובה.
התוכנית תבדוק אם התשובה נכונה.
עבור כל תשובה נכונה המשתמש יקבל נקודה.
בסיום יוצג הציון הסופי.
""")
    elif val == "3":
        break

