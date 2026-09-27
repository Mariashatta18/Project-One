import json
# Student Assignment and Grade Tracker

assignments = []

print("Student Assignment and Grade Tracker")

while True:
    print("\n1. Add Assignment")
    print("2. View Assignments")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter assignment name: ")
        grade = input("Enter grade: ")

        assignment = {
            "name": name,
            "grade": grade
        }

        assignments.append(assignment)
        print("Assignment added.")

    elif choice == "2":
        if len(assignments) == 0:
            print("No assignments added yet.")
        else:
            for assignment in assignments:
                print(assignment["name"], "-", assignment["grade"])

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Please choose 1, 2, or 3.")
