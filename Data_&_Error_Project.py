import copy
# Global data
students = []          # List to store students
unique_rolls = set()   # Set to avoid duplicate roll numbers
# Functions
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
        student = {
            "name": name,
            "roll": roll,
            "marks": dict(zip(subjects, marks))  # (zip + dict)
        }
        students.append(student)    # (list)
        unique_rolls.add(roll)      # (set)
        print("Student added successfully!")
    except Exception as e:
        print("Error:", e)
def display_students():
    if not students:
        print("No students available")
        return
    print("\nStudent List:")
    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}")
def search_student():
    search = input("Enter roll or name to search: ").title()
    found = False
    for s in students:
        if str(s["roll"]) == search or s["name"] == search:
            print(f"Found: {s}")
            found = True
    if not found:
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
                else:
                    print("Invalid subject")
                    return
        print("Roll not found")
    except ValueError:
        print("Invalid input")
# (List comprehension)
def toppers_math():
    top = [s for s in students if s["marks"]["Math"] > 90]
    print("Toppers in Math:", top)
def toppers_science():
    top = [s for s in students if s["marks"]["Science"] > 90]
    print("Toppers in Science:", top)
def toppers_english():
    top = [s for s in students if s["marks"]["English"] > 90]
    print("Toppers in English:", top)
def backup_data():
    # Day 20 (Deep copy)
    backup = copy.deepcopy(students)
    print("Backup created:", backup)
# Menu Driven Program
while True:
    print("\n====== Student Management System ======")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Show Toppers in Math")
    print("6. Show Toppers in Science")
    print("7. Show Toppers in English")
    print("8. Create Backup (Deep Copy)")
    print("9. Exit")
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
        toppers_math()
    elif choice == "6":
        toppers_science()
    elif choice == "7":
        toppers_english()
    elif choice == "8":
        backup_data()
    elif choice == "9":
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again.")
