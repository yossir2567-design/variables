arr = [10,20,30,40,50]
print(arr)
print(arr[0])
print(arr[-1])
print(arr[2])


students = ["Noa", "Itay", "Maya", "Daniel", "Tamar", "Omer", "Shira"]
print(len(students))
print(students[0], students[-1])
students[1] = "Moty"
print(students)


grades = [50,70,80,95,100]
grades.append(98)
grades.insert(0, 87)
grades[2] = 68
print(grades)



numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
numbers.pop(0)
print(numbers)
numbers.pop()
print(numbers)
numbers.pop(2)
print(numbers)


products = ["Laptop", "Smartphone", "Headphones", "Keyboard", "Mouse", "Monitor"]
print("The laptop is on the list." if "Laptop" in products else "The laptop is NOt on the list.")
print("The Mouse is Not on the list." if "Mouse" not in products else "The Mouse is on the list.")



numbers = [1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    print(i)


numbers = [1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    if i % 2 == 0:
        print(i)




grades = [50,70,80,95,100]
sub = 0
for n in grades:
    sub += n
print(sub)




numbers = [50,70,80,95,100, 52, 89]
max_num = 0
for i in numbers:
    if i > max_num:
        max_num = i
print(max_num)




students = ["Noa", "Itay", "Maya", "Daniel", "Tamar", "Omer", "Shira"]
name = input("Enter name: ")
flag = "Not Found"
for n in students:
    if n == name:
        flag = "Found"
        break
print(flag)





numbers = [50,70,80,95,100, 52, 89]
search = int(input("Enter number: "))
for i in range(len(numbers)):
    if numbers[i] == search:
        print(i)
        break





numbers = [50,70,80,95,100, 52, 89]
count = 0
for i in numbers:
    if i > 50:
        count +=1
print(count)


numbers = [1,2,3,4,5,6,7,8,9,10]
even_list = []
for i in numbers:
    if i % 2 == 0:
        even_list.append(i)
print(even_list)



students = ["Noa", "Itay", "Maya", "Daniel", "Tamar", "Omer", "Shira"]
name = 0
while name < len(students):
    print(students[name], name)
    name += 1



numbers = [10, 20, 30, 40, 50, 60]
print(numbers[:3])
print(numbers[3:])
print(numbers[2:6])
print(numbers[::-1])




students = ["Noa", "Itay", "Maya", "Daniel", "Tamar", "Omer", "Shira"]
for i in range(len(students)):
    if i % 2 == 0:
        print(students[i])
print(students[::-2])


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
first = numbers[:10]
secound = numbers[10:]
print(first)
print(secound)






numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
double = [num * 2 for num in numbers]
multy = [num * num for num in numbers]
even = [num for num in numbers if num % 2 == 0]
five = [num for num in numbers if num > 5]




grades = [55, 90, 67, 100, 45, 82, 73, 30]
passed = [pas for pas in grades if pas >= 60]
failed = [fa for fa in grades if fa < 60]
add_five = [num + 5 for num in grades]




names = ["Moshe", "David", "Dana", "Noa", "Michael", "Avi"]
four = [name for name in names if len(name) > 4]
up = [name.upper() for name in names]
d_list = [name for name in names if name[0] == "D"]





numbers = [12, 7, 25, 30, 9, 44, 18, 3]
new = [num for num in numbers if num % 3 == 0 and num > 10]




numbers = []
for i in range(10):
    val = int(input("Ente rnumber: "))
    numbers.append(val)
print(numbers)
min_num = float('inf')
max_num = float('-inf')
for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print(max_num)
print(min_num)
print(sum(numbers)/len(numbers))


students = ["Liam", "Emma", "Noah", "Olivia", "Ethan", "Sophia", "Lucas"]
val = input("Enter student: ")
if val in students:
    students.remove(val)
else:
    print("Not found Student")
print(students)


numbers = [5, 12, 23, 8, 34, 17, 42, 19, 28, 3]

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
greater_20 = [num for num in numbers if num > 20]
print(even_numbers)
print(odd_numbers)
print(greater_20)


numbers = [10, 25, 7, 25, 40, 12, 25, 9]
target = int(input("Enter number: "))

positions = []
for i in range(len(numbers)):
    if numbers[i] == target:
        positions.append(i)
    print(len(positions))



list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8, 9, 10]
list3 = list1 + list2
print(list3)
print(list3[:5])
print(list3[:5])
print(list3[::-1])


numbers = [4, 11, 22, 35, 48]
new_num = int(input("Enter a number: "))

flag = False
for num in numbers:
    if num == new_num:
        flag = True
        break
if not flag:
    numbers.append(new_num)
    print("it's new")
else:
    print("it's already exists")
print(numbers)





grades = [85, 72, 90, 55, 100, 63, 48, 77]
while True:
    val = input("""
===== Grades Management =====

1. Show all grades
2. Add a grade
3. Search for a grade
4. Remove a grade
5. Show passing grades
6. Show failing grades
7. Show highest and lowest grade
8. Show average grade
9. Show first 3 grades
10. Show grades in reverse
0. Exit
your choice: """)
    if val=="1":
        for grade in grades:
            print(grade)
    elif val=="2":
        score = int(input("Enter Score: "))
        grades.append(score)
        for g in grades:
            print(g)
    elif val=="3":
        search = int(input("Enter grade: "))
        for n in range(len(grades)):
            if grades[n] == search:
                print(n)
    elif val=="4":
        rem = int(input("Enter Score: "))
        if rem in grades:
            grades.remove(rem)
    elif val=="5":
        passed = [g for g in grades if g >= 60]
        for x in passed:
            print(x)
    elif val=="6":
        faild = [g for g in grades if g < 60]
        for f in faild:
            print(f)
    elif val=="7":
        min_num = float('inf')
        max_num = float('-inf')
        for s in grades:
            if s < min_num:
                min_num = s
            if s > max_num:
                max_num = s
        print(max_num)
        print(min_num)
    elif val=="8":
        total = 0
        for s in grades:
            total += s
            print(total/len(grades))
    elif val=="9":
        print(grades[:3])
    elif val=="10":
        print(grades[::-1])
    elif val=="0":
        print("Good Bay")
        break                     
                            