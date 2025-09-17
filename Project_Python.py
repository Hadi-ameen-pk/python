import re

students = []
unique_rolls = set()
user_data = {}

# Email validation regex
pattern = r"[a-z0-9]+@[a-zA-Z]+\.(com|in|org)"

# ---------- Register User ----------
def register():
    print("=== Create Account ===")
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
    print("=== Sign In ===")
    for _ in range(3):
        e = input("Enter email: ")
        p = input("Enter password: ")
        if e == user_data.get("email") and p == user_data.get("password"):
            print("Login successful!\n")
            return True
        else:
            print("Invalid credentials, try again.")
    print("Too many failed attempts. Exiting...")
    backup_data()   # Auto-save on failed login
    return False

# ---------- Logout ----------
def logout():
    print("Logging out...")
    backup_data()
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
        while True:
            name = input("Enter student name: ").strip().title()
            if not name:
                print("Name cannot be empty!")
            elif not all(x.isalpha() or x.isspace() for x in name):
                print("Name must contain only letters and spaces!")
            else:
                break

        roll = int(input("Enter roll number: "))
        if roll in unique_rolls:
            print("Roll number already exists!")
            return

        marks = {}
        while True:
            subject = input("Enter subject name (or press Enter to finish): ").title()
            if subject == "":
                break
            try:
                m = int(input(f"Enter marks for {subject}: "))
            except ValueError:
                print("Invalid input, setting marks = 0")
                m = 0
            marks[subject] = m

        if not marks:
            print("No subjects entered, student not added.")
            return

        student = {"name": name, "roll": roll, "marks": marks}
        students.append(student)
        unique_rolls.add(roll)
        print("Student added successfully!")

    except Exception as e:
        print("Error:", e)

# ---------- Display Students (Sorted by Roll No) ----------
def display_students():
    if not students:
        print("No students available")
        return
    sorted_students = sorted(students, key=lambda s: s['roll'])
    for s in sorted_students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}")

# ---------- Search Student ----------
def search_student():
    search = input("Enter roll or name to search: ").title()
    for s in students:
        if str(s["roll"]) == search or s["name"] == search:
            print("Found:", s)
            return
    print("Student not found")

# ---------- Update Marks ----------
def update_marks():
    try:
        roll = int(input("Enter roll number to update: "))
        for s in students:
            if s["roll"] == roll:
                subject = input("Enter subject name: ").title()
                if subject in s["marks"]:
                    new_mark = int(input(f"Enter new marks for {subject}: "))
                    s["marks"][subject] = new_mark
                    print("Marks updated successfully!")
                    return
                print("Subject not found for this student")
                return
        print("Roll not found")
    except ValueError:
        print("Invalid input")

# ---------- Remove Subject ----------
def remove_subject():
    try:
        roll = int(input("Enter roll number of the student: "))
        for s in students:
            if s["roll"] == roll:
                if not s["marks"]:
                    print("No subjects to remove for this student.")
                    return
                print(f"Subjects available: {', '.join(s['marks'].keys())}")
                subject = input("Enter subject to remove: ").title()
                if subject in s["marks"]:
                    del s["marks"][subject]
                    print(f"Subject '{subject}' removed successfully!")
                else:
                    print("Subject not found for this student")
                return
        print("Roll not found")
    except ValueError:
        print("Invalid input")

# ---------- Topper Function (Sorted by Marks Desc) ----------
def topper():
    if not students:
        print("No students available")
        return

    subject = input("Enter subject to find topper: ").title()
    available_subjects = {sub for s in students for sub in s["marks"]}
    if subject not in available_subjects:
        print(f"No student has subject '{subject}'.")
        return

    students_with_subject = [s for s in students if subject in s["marks"]]
    sorted_students = sorted(students_with_subject, key=lambda s: s["marks"][subject], reverse=True)

    highest_mark = sorted_students[0]["marks"][subject]
    top_students = [s for s in sorted_students if s["marks"][subject] == highest_mark]

    print(f"\nTopper(s) in {subject}:")
    for s in top_students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks'][subject]}")

# ---------- Backup Data (Avoid Duplicate Backups) ----------
def backup_data():
    backup_str = "\n=== Backup Data ===\n"
    backup_str += "User:\n"
    backup_str += f"Email: {user_data.get('email', '')}\n"
    backup_str += f"Password: {user_data.get('password', '')}\n\n"
    backup_str += "Students:\n"
    for s in students:
        backup_str += f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}\n"

    try:
        with open("backup.txt", "r") as f:
            existing_data = f.read()
    except FileNotFoundError:
        existing_data = ""

    if backup_str.strip() in existing_data:
        print("Backup already exists, skipping duplicate entry.")
        return

    with open("backup.txt", "a") as f:
        f.write(backup_str)
    print("Backup saved to backup.txt")

# ---------- Load Backup ----------
def load_backup():
    global students, unique_rolls, user_data
    try:
        with open("backup.txt", "r") as f:
            lines = f.readlines()
        current_section = None
        students = []
        user_data = {}
        for line in lines:
            line = line.strip()
            if line.startswith("User:"):
                current_section = "user"
            elif line.startswith("Students:"):
                current_section = "students"
            elif current_section == "user" and line.startswith("Email:"):
                user_data["email"] = line.split("Email:")[1].strip()
            elif current_section == "user" and line.startswith("Password:"):
                user_data["password"] = line.split("Password:")[1].strip()
            elif current_section == "students" and line.startswith("Roll:"):
                parts = line.split(",")
                roll = int(parts[0].split("Roll:")[1].strip())
                name = parts[1].split("Name:")[1].strip()
                marks_str = ",".join(parts[2:]).split("Marks:")[1].strip()
                marks = {}
                for m in marks_str.strip("{} ").split(","):
                    if ":" in m:
                        key, val = m.split(":")
                        marks[key.strip().strip("'").strip('"')] = int(val.strip())
                students.append({"name": name, "roll": roll, "marks": marks})
        unique_rolls = {s["roll"] for s in students}
        if students or user_data:
            print("Backup loaded successfully!")
    except FileNotFoundError:
        print("No backup found, starting fresh.")

# ---------- Main Program ----------
load_backup()
print("\n=== Welcome to Student Management System ===")
print("1. Register (new user)")
print("2. Login (existing user)")
choice = input("Enter choice: ")

if choice == "1":
    user_data = register()
elif choice == "2":
    if not user_data:
        print("No existing user found, please register first.")
        user_data = register()
else:
    print("Invalid choice, defaulting to Register.")
    user_data = register()

if login(user_data):
    while True:
        print("\n====== Student Management System ======")
        print("1. Add Student")
        print("2. Display Students (Sorted by Roll No)")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Show Topper in a Subject (Sorted by Marks Desc)")
        print("6. Create Backup")
        print("7. Change Email")
        print("8. Change Password")
        print("9. Remove Subject")
        print("10. Logout")
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
            topper()
        elif choice == "6":
            backup_data()
        elif choice == "7":
            change_email(user_data)
        elif choice == "8":
            change_password(user_data)
        elif choice == "9":
            remove_subject()
        elif choice == "10":
            if not logout():
                print("You have been logged out.")
                break
        elif choice == "11":
            print("Saving data before exit...")
            backup_data()
            print("Exiting program...")
            break

        else:
            print("Invalid choice, try again.")
