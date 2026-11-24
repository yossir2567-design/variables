def say_hello():
    print("Hello World")
for i in range(3):
    say_hello()

def show_welcome():
    print("Welcome")
show_welcome()


def show_menu():
    print("""
===== Main Menu =====
1. Start
2. Settings
3. Exit""")
show_menu()


def show_number():
    for i in range(1,11):
        print(i)
show_number()



def show_even_numbers():
    for i in range(1,101):
        if i % 2 == 0:
            print(i)
show_even_numbers()


def show_stars():
    for i in range(5):
        print("*"*10)
show_stars()




def greet(name):
    print("Welcome " + name)



def show_age(age):
    print(f"Your age: {age}")


def calculate_sum(num1, num2):
    print(num1+num2)

def calculate_average(g1, g2, g3):
    print((g1+g2+g3)/3)

def check_even(num):
    print("Even" if num % 2 == 0 else "Odd")
def check_password(password):
    if password == 123456:
        print("Access Granted.")
    else:
        print("Access Denied.")

def calculate_discount(price, discount):
    total_dis = 1- discount/100
    print(price * total_dis)

def show_range(num1, num2):
    for i in range(num1+1, num2):
        print(i)

def print_rectangle(height, width):
    for i in range(height):
        print("*"*width)



def multiply(num1, num2):
    return num1 * num2

def get_full_name(first_name, last_name):
    return f"{first_name} - {last_name}"

def get_max(num1, num2):
    if num1>num2:
        return num1
    else:
        return num2

def is_positive(num):
    return num > 0

def calculate_tax(price, vat):
    return price + price * vat

def get_grade_status(grade):
    if 90 <= grade <= 100:
        mes = "Excellent"
    elif grade >= 75:
        mes = "Good"
    elif grade >= 60:
        mes = "Average"
    elif grade >= 0:
        mes = "Failed"
    return mes

def count_digits(num):
    return len(str(num))


def calculate_power(num1, num2):
    total = 1
    for i in range(num2):
        total = total * num1
    return total



def print_list(arr):
    print(*arr, sep="\n")
print_list([1,2,3,4,5,6,7,8,9])


def get_list_sum(arr:list)->int:
    total = 0
    for i in arr:
        total += i
    return total

def get_list_average(arr:list)->float:
    if not arr:
        return "The arr is amty"
    return sum(arr)/len(arr)

def find_number(numbers:list, num)->bool:
    for n in numbers:
        if n == num:
            return True
    return False



def find_max(arr)->int:
    max_n = float('-inf')
    for n in arr:
        if n > max_n:
            max_n = n
    return max_n

def get_even_numbers(arr):
    return [n for n in arr if n % 2 == 0]



def get_long_names(names):
    return [name for name in names if len(name) > 4]


def reverse_list(arr):
    return arr[::-1]


def count_occurrences(numbers:list, num):
    return numbers.count(num)


def remove_duplicates(arr):
    new_list = []
    for i in arr:
        if i not in new_list:
            new_list.append(i)
    return new_list


def calculate_final_price(price, dis):
    discount = dis/100
    check = price * (1-discount)
    if check > 500:
        discount+=0.05
        return price * (1-discount)
    return check


def check_list(numbers):
    evens = 0
    odd = 0
    for n in numbers:
        if n % 2 == 0:
            evens += 1
        else:
            odd += 1
    return evens, 0dd, sum(numbers)


def analyze_grades(grades:list):
    average = sum(grades)/len(grades)
    max_grade = max(grades)
    min_grade = min(grades)
    passed = 0
    for g in grades:
        if g > 60:
            passed += 1
    return average, max_grade, min_grade, passed


def validate_user(user, password):
    return len(user.strip()) > 0 and len(password) >= 6


def search_students(students, name):
    for s in students:
        if s["name"] == name:
            return s
    return None



def calculate_cart_total(cart):
    return sum(p["price"] * p["quantity"] for p in cart)


def get_fibonacci(n):
    a = 0
    b = 1
    c = a+b
    fibonacci = []
    for i in range(n):
        fibonacci.append(a)
        a = b
        b = c
        c = a+b
    return fibonacci
print(get_fibonacci(7))


name = "David"
def show_name():
	name = "Moshe"
print(name)  #David
show_name()
print(name)  #David


counter = 10
def increase():
	counter = 20
	print(counter)
increase()
print(counter)
# בגלל שזה משתנה פנימי ולא גלובלי



def add_ten(num):
    num += 10
    return num
num = 5
print(add_ten(num))
print(num)


def add_in_arr(arr):
    arr.append(5)
    print(arr)
arr = [1,2,3,4]
print(arr)
add_in_arr(arr)
print(arr) # בגלל שזה לא משתנה פנימי אלא תא זיכרון שמור גלובלי 


def slicing_arr(arr):
    new_list = arr[::1]
    new_list.append(5)
    return(new_list)
arr = [1,2,3,4]
print(arr)
print(slicing_arr(arr))
print(arr)        









def show_menu():
    val = input("""
===== Student Management =====

1. Show all students
2. Add student
3. Search student
4. Update student grade
5. Remove student
6. Show passing students
7. Show class statistics
8. Show students above average
0. Exit
Your choice: """)
    return val


def show_students(students):
    if not students:
        return "The list is empty"
    return students  

def add_student(students):
    student = {"name":input("Enter name: "), "age":int(input("Enter age: ")), "grade":int(input("Enter grade: "))}
    students.append(student)

def search_student(students, name):
    if not students:
        return "The list is empty"
    for student in students:
        if student["name"] == name:
            return student
    return "Name not found"
def update_grade(students, name, grade):
    if not students:
        return "The list is empty"
    for student in students:
        if student["name"] == name:
            student["grade"] = grade
            return "Grade updated successfully"
    return "Name not found"
def remove_student(students:list, name):
    if not students:
        return "The list is empty"
    for student in students:
        if student["name"] == name:
            students.remove(student)
            return "Student successfully removed"
    return "Name not found"
def get_passing_students(students):
    if not students:
        return "The list is empty"
    return [s for s in students if s["grade"] > 60]

def get_average(students):
    if not students:
        return "The list is empty"
    return sum(s["grade"] for s in students)/len(students)

def get_highest_grade(students):
    if not students:
        return "The list is empty"
    return max(s["grade"] for s in students)


def show_statistics(students):
    if not students:
        return "The list is empty"
    return f"Average: {get_average(students)}\nHighest Score: {get_highest_grade(students)}"




students = [
    {"name": "David", "age": 20, "grade": 90},
    {"name": "Moshe", "age": 22, "grade": 75},
    {"name": "Dana", "age": 21, "grade": 100},
    {"name": "Noa", "age": 19, "grade": 55},
    {"name": "Avi", "age": 23, "grade": 82}
    ]
while True:
    val = show_menu()
    if val == "1":
        print(show_students(students))
    elif val == "2":
        add_student(students)
    elif val == "3":
        print(search_student(students, input("Enter name: ")))
    elif val == "4":
        print(update_grade(students, input("Enter name: ") , int(input("Enter grade: "))))
    elif val == "5":
        print(remove_student(students, input("Enter name: ")))
    elif val == "6":
        print(get_passing_students(students))
    elif val == "7":
        print(show_statistics(students))
    elif val == "8":
        print(get_average(students))
    elif val == "0":
        break
