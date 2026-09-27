import json

# Student Assignment and Grade Tracker

try:
    with open("assignments.json", "r") as file:
        courses = json.load(file)
except FileNotFoundError:
    courses = {}

print("Student Assignment and Grade Tracker")

while True:
    print("\n1. Add Course")
    print("2. Add Assignment and Grade")
    print("3. View Courses and Grades")
    print("4. Calculate Average Grade")
    print("5. Check Passing Status")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        course = input("Enter course name: ")

        if course not in courses:
            courses[course] = []
            print("Course added.")
        else:
            print("Course already exists.")

    elif choice == "2":
        course = input("Enter course name: ")

        if course not in courses:
            print("Course not found. Add the course first.")
        else:
            assignment_name = input("Enter assignment name: ")
            grade = float(input("Enter grade: "))

            assignment = {
                "name": assignment_name,
                "grade": grade
            }

            courses[course].append(assignment)

            with open("assignments.json", "w") as file:
                json.dump(courses, file)

            print("Assignment and grade added.")

    elif choice == "3":
        if len(courses) == 0:
            print("No courses added yet.")
        else:
            for course in courses:
                print("\nCourse:", course)

                if len(courses[course]) == 0:
                    print("No assignments yet.")
                else:
                    for assignment in courses[course]:
                        print(assignment["name"], "-", assignment["grade"])

    elif choice == "4":
        course = input("Enter course name: ")

        if course not in courses:
            print("Course not found.")
        elif len(courses[course]) == 0:
            print("No grades available.")
        else:
            total = 0

            for assignment in courses[course]:
                total += assignment["grade"]

            average = total / len(courses[course])
            print("Average grade:", round(average, 2))

    elif choice == "5":
        course = input("Enter course name: ")

        if course not in courses:
            print("Course not found.")
        elif len(courses[course]) == 0:
            print("No grades available.")
        else:
            total = 0

            for assignment in courses[course]:
                total += assignment["grade"]

            average = total / len(courses[course])

            if average >= 60:
                print("The student is passing.")
            else:
                print("The student is not passing.")

    elif choice == "6":
        with open("assignments.json", "w") as file:
            json.dump(courses, file)

        print("Goodbye!")
        break

    else:
        print("Please choose a number from 1 to 6.")
