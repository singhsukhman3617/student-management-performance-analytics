
from functio import add_student, view_students, search_student, add_course, enroll_student, add_marks, view_student_performance, department_performance_summary, top_students_ranking

def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. add course")
        print("5. enroll new student in course")
        print("6. record student marks")
        print("7. view student performance")
        print("8. department performance summary")
        print("9. top student ranking")
        print("10. exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            add_course()

        elif choice == "5":
            enroll_student()

        elif choice == "6":
            add_marks()

        elif choice == "7":
            view_student_performance()

        elif choice == "8":
            department_performance_summary()

        elif choice == "9":
            top_students_ranking()

        elif choice == "10":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
