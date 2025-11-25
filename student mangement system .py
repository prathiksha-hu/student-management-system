import json
import os

FILE_NAME = "student.txt"


class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def to_dict(self):
        return {"roll": self.roll, "name": self.name, "marks": self.marks}


class StudentManagementSystem:

    def __init__(self):
        if not os.path.exists(FILE_NAME):
            with open(FILE_NAME, "w") as f:
                f.write("[]")

    def load_data(self):
        with open(FILE_NAME, "r") as f:
            return json.load(f)

    def save_data(self, data):
        with open(FILE_NAME, "w") as f:
            json.dump(data, f, indent=4)

    # ---------------------------------------
    # Add New Student
    # ---------------------------------------
    def add_student(self):
        try:
            roll = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            marks = float(input("Enter Marks: "))

            student = Student(roll, name, marks).to_dict()
            data = self.load_data()
            data.append(student)
            self.save_data(data)

            print("Student Added Successfully!\n")
        except:
            print("Error: Invalid input!")

    # ---------------------------------------
    # View All Students
    # ---------------------------------------
    def view_students(self):
        data = self.load_data()
        if not data:
            print("No record found.\n")
            return

        print("\n---- Student Records ----")
        for s in data:
            print(s)
        print()

    # ---------------------------------------
    # Search Students
    # ---------------------------------------
    def search_student(self):
        roll = input("Enter Roll Number to Search: ")
        data = self.load_data()

        for s in data:
            if s["roll"] == roll:
                print("Student Found:", s, "\n")
                return

        print("Student Not Found.\n")

    # ---------------------------------------
    # Update Student
    # ---------------------------------------
    def update_student(self):
        roll = input("Enter Roll Number to Update: ")
        data = self.load_data()

        for s in data:
            if s["roll"] == roll:
                s["name"] = input("Enter New Name: ")
                s["marks"] = float(input("Enter New Marks: "))
                self.save_data(data)
                print("Student Updated Successfully!\n")
                return

        print("Student Not Found.\n")

    # ---------------------------------------
    # Delete Student
    # ---------------------------------------
    def delete_student(self):
        roll = input("Enter Roll Number to Delete: ")
        data = self.load_data()

        new_data = [s for s in data if s["roll"] != roll]

        if len(new_data) == len(data):
            print("Student Not Found.\n")
        else:
            self.save_data(new_data)
            print("Student Deleted Successfully!\n")

    # ---------------------------------------
    # Calculate Average & Find Topper
    # ---------------------------------------
    def calculate_topper(self):
        data = self.load_data()
        if not data:
            print("No Students Available!\n")
            return

        total = sum(s["marks"] for s in data)
        avg = total / len(data)

        topper = max(data, key=lambda x: x["marks"])

        print(f"\nClass Average = {avg}")
        print("Topper =", topper, "\n")


# =======================================
# ----------- MAIN PROGRAM --------------
# =======================================

sms = StudentManagementSystem()

while True:
    print("\n===== STUDENT MANAGEMENT MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Average & Topper")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sms.add_student()
    elif choice == "2":
        sms.view_students()
    elif choice == "3":
        sms.search_student()
    elif choice == "4":
        sms.update_student()
    elif choice == "5":
        sms.delete_student()
    elif choice == "6":
        sms.calculate_topper()
    elif choice == "7":
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice!\n")
