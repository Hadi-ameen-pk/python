import copy
import re
import json

students = []
unique_rolls = set()

# Email validation regex
pattern = r"[a-z0-9]+@[a-zA-Z]+\.(com|in|org)"

# ---------- Register User ----------
def register():
    print("=== User Registration ===")
    while True:
        email = input("Set email: ")
        if re.fullmatch(pattern, email):
            break
        else:
            print("Invalid email format! Please try again.")

    while True:
        password = input("Set password: ")
        if len(password) < 6:
            print("Invalid password (too short, must be at least 6 characters)")
        elif password.isdigit():
            print("Invalid password (cannot be only numbers)")
        elif password.isalpha():
            print("Invalid password (cannot be only letters)")
        else:
            break

    print("Registration successful!\n")
    return {"email": email, "password": password}

# ---------- Login ----------
def login(user_data):
    for _ in range(3):
        e = input("Enter email: ")
        p = input("Enter password: ")
        if e == user_data["email"] and p == user_data["password"]:
            print("Login successful!\n")
            return True
        else:
            print("Invalid credentials, try again.")
    print("Too many failed attempts. Exiting...")
    return False

# ---------- Change Email ----------
def change_email(user_data):
    while True:
        new_email = input("Enter new email: ")
        if re.fullmatch(pattern, new_email):
            user_data["email"] = new_email
            print("Email changed successfully!")
            break
        else:
            print("Invalid email format! Try again.")

# ---------- Change Password ----------
def change_password(user_data):
    while True:
        new_pass = input("Enter new password: ")
        if len(new_pass) < 6:
            print("Invalid password (too short, must be at least 6 characters)")
        elif new_pass.isdigit():
            print("Invalid password (cannot be only numbers)")
        elif new_pass.isalpha():
            print("Invalid password (cannot be only letters)")
        else:
            user_data["password"] = new_pass
            print("Password changed successfully!")
            break

# ---------- Student Functions ----------
def add_student():
    try:
        name = input("Enter student name: ").title()
        roll = int(input("Enter roll number: "))
        if roll in unique_rolls:
            print("Roll number already exists!")
            return
        subjects = ["Math", "Science", "English"]
        marks = []
        for sub in subjects:
            try:
                m = int(input(f"Enter marks for {sub}: "))
                marks.append(m)
            except ValueError:
                print("Invalid input, setting marks = 0")
                marks.append(0)
        student = {"name": name, "roll": roll, "marks": dict(zip(subjects, marks))}
        students.append(student)
        unique_rolls.add(roll)
        print("Student added successfully!")
    except Exception as e:
        print("Error:", e)

def display_students():
    if not students:
        print("No students available")
        return
    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}")

def search_student():
    search = input("Enter roll or name to search: ").title()
    for s in students:
        if str(s["roll"]) == search or s["name"] == search:
            print("Found:", s)
            return
    print("Student not found")

def update_marks():
    try:
        roll = int(input("Enter roll number to update: "))
        for s in students:
            if s["roll"] == roll:
                subject = input("Enter subject (Math/Science/English): ").title()
                if subject in s["marks"]:
                    new_mark = int(input(f"Enter new marks for {subject}: "))
                    s["marks"][subject] = new_mark
                    print("Marks updated successfully!")
                    return
                print("Invalid subject")
                return
        print("Roll not found")
    except ValueError:
        print("Invalid input")

# ---------- Topper Function ----------
def topper(subject):
    if not students:
        print("No students available")
        return

    # Find highest mark in subject
    highest = max(s["marks"][subject] for s in students)

    # Get all students with that mark
    top_students = [s for s in students if s["marks"][subject] == highest]

    print(f"\nTopper(s) in {subject}:")
    for s in top_students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks'][subject]}")

def backup_data():
    with open("students_backup.json", "w") as f:
        json.dump(students, f, indent=4)
    print("Backup saved to students_backup.json")

# ---------- Main Program ----------
user_data = register()

if login(user_data):
    while True:
        print("\n====== Student Management System ======")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Show Topper in Math")
        print("6. Show Topper in Science")
        print("7. Show Topper in English")
        print("8. Create Backup")
        print("9. Change Email")
        print("10. Change Password")
        print("11. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            topper("Math")
        elif choice == "6":
            topper("Science")
        elif choice == "7":
            topper("English")
        elif choice == "8":
            backup_data()
        elif choice == "9":
            change_email(user_data)
        elif choice == "10":
            change_password(user_data)
        elif choice == "11":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.")
