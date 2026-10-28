
from db import get_connection


def add_student():
    print("\n--- Add New Student ---")

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    department = input("Enter department: ")
    admission_date = input("Enter admission date (YYYY-MM-DD): ")

    connection = get_connection()

    if connection is None:
        print("Unable to connect to database.")
        return

    cursor = connection.cursor()

    query = """
        INSERT INTO STUDENT
        (FIRST_NAME, LAST_NAME, EMAIL, DEPARTMENT, ADMISSION_DATE)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        first_name,
        last_name,
        email,
        department,
        admission_date
    )

    try:
        cursor.execute(query, values)
        connection.commit()
        print("Student added successfully!")

    except Exception as error:
        connection.rollback()
        print("Error adding student:", error)

    finally:
        cursor.close()
        connection.close()


def view_students():
    print("\n--- All Students ---")

    connection = get_connection()

    if connection is None:
        print("Unable to connect to database.")
        return

    cursor = connection.cursor()

    query = """
        SELECT STUDENT_ID, FIRST_NAME, LAST_NAME,
               EMAIL, DEPARTMENT, ADMISSION_DATE
        FROM STUDENT
        ORDER BY STUDENT_ID
    """

    try:
        cursor.execute(query)
        students = cursor.fetchall()

        if not students:
            print("No students found.")
            return

        for student in students:
            print("-" * 50)
            print(f"ID: {student[0]}")
            print(f"Name: {student[1]} {student[2]}")
            print(f"Email: {student[3]}")
            print(f"Department: {student[4]}")
            print(f"Admission Date: {student[5]}")

    except Exception as error:
        print("Error fetching students:", error)

    finally:
        cursor.close()
        connection.close()



def search_student():
    print("\n--- Search Student ---")

    student_id = input("Enter Student ID: ")

    connection = get_connection()

    if connection is None:
        print("Unable to connect to database.")
        return

    cursor = connection.cursor()

    query = """
        SELECT STUDENT_ID, FIRST_NAME, LAST_NAME,
               EMAIL, DEPARTMENT, ADMISSION_DATE
        FROM STUDENT
        WHERE STUDENT_ID = %s
    """

    try:
        cursor.execute(query, (student_id,))
        student = cursor.fetchone()

        if student:
            print("\nStudent Found!")
            print("-" * 40)
            print(f"ID: {student[0]}")
            print(f"Name: {student[1]} {student[2]}")
            print(f"Email: {student[3]}")
            print(f"Department: {student[4]}")
            print(f"Admission Date: {student[5]}")
        else:
            print("No student found with that ID.")

    except Exception as error:
        print("Error searching for student:", error)

    finally:
        cursor.close()
        connection.close()


def add_course():
    print("\n--- Add New Course ---")

    course_name = input("Enter course name: ")
    course_code = input("Enter course code: ")
    credits = input("Enter course credits: ")

    connection = get_connection()

    if connection is None:
        print("Unable to connect to database.")
        return

    cursor = connection.cursor()

    query = """
        INSERT INTO COURSES (COURSE_NAME, COURSE_CODE, CREDITS)
        VALUES (%s, %s, %s)
    """

    values = (course_name, course_code, credits)

    try:
        cursor.execute(query, values)
        connection.commit()
        print("Course added successfully!")

    except Exception as error:
        connection.rollback()
        print("Error adding course:", error)

    finally:
        cursor.close()
        connection.close()


def enroll_student():
    print("\n--- Enroll Student in a Course ---")

    student_id = input("Enter Student ID: ")
    course_id = input("Enter Course ID: ")
    enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")

    connection = get_connection()

    if connection is None:
        print("Unable to connect to database.")
        return

    cursor = connection.cursor()

    query = """
        INSERT INTO ENROLLMENTS
        (STUDENT_ID, COURSE_ID, ENROLLMENT_DATE)
        VALUES (%s, %s, %s)
    """

    values = (student_id, course_id, enrollment_date)

    try:
        cursor.execute(query, values)
        connection.commit()
        print("Student enrolled successfully!")

    except Exception as error:
        connection.rollback()
        print("Error enrolling student:", error)

    finally:
        cursor.close()
        connection.close()


def add_marks():
    print("\n--- Record Student Marks ---")

    student_id = input("Enter Student ID: ")
    course_id = input("Enter Course ID: ")
    marks_obtained = input("Enter marks obtained: ")
    max_marks = input("Enter maximum marks: ")
    exam_date = input("Enter exam date (YYYY-MM-DD): ")

    connection = get_connection()

    if connection is None:
        print("Unable to connect to database.")
        return

    cursor = connection.cursor()

    query = """
        INSERT INTO MARKS
        (STUDENT_ID, COURSE_ID, MARKS_OBTAINED, MAX_MARKS, EXAM_DATE)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        student_id,
        course_id,
        marks_obtained,
        max_marks,
        exam_date
    )

    try:
        cursor.execute(query, values)
        connection.commit()
        print("Marks recorded successfully!")

    except Exception as error:
        connection.rollback()
        print("Error recording marks:", error)

    finally:
        cursor.close()
        connection.close()


def view_student_performance():
    print("\n--- Student Course-wise Performance ---")

    student_id = input("Enter Student ID: ")

    connection = get_connection()

    if connection is None:
        print("Unable to connect to database.")
        return

    cursor = connection.cursor()

    query = """
        SELECT
            s.FIRST_NAME,
            s.LAST_NAME,
            c.COURSE_NAME,
            m.MARKS_OBTAINED,
            m.MAX_MARKS,
            ROUND(
                (m.MARKS_OBTAINED / m.MAX_MARKS) * 100, 2
            ) AS PERCENTAGE
        FROM STUDENT s
        JOIN ENROLLMENTS e
            ON s.STUDENT_ID = e.STUDENT_ID
        JOIN COURSES c
            ON e.COURSE_ID = c.COURSE_ID
        JOIN MARKS m
            ON m.STUDENT_ID = e.STUDENT_ID
            AND m.COURSE_ID = e.COURSE_ID
        WHERE s.STUDENT_ID = %s
        ORDER BY c.COURSE_NAME
    """

    try:
        cursor.execute(query, (student_id,))
        results = cursor.fetchall()

        if results:
            print(f"\nPerformance for {results[0][0]} {results[0][1]}")
            print("-" * 65)

            for row in results:
                print(f"Course: {row[2]}")
                print(f"Marks: {row[3]} / {row[4]}")
                print(f"Percentage: {row[5]}%")
                print("-" * 65)
        else:
            print("No performance records found for this student.")

    except Exception as error:
        print("Error fetching performance:", error)

    finally:
        cursor.close()
        connection.close()



def department_performance_summary():
    print("\n--- Department-wise Performance Summary ---")

    connection = get_connection()

    if connection is None:
        print("Unable to connect to database.")
        return

    cursor = connection.cursor()

    query = """
        SELECT
            s.DEPARTMENT,
            COUNT(DISTINCT s.STUDENT_ID) AS TOTAL_STUDENTS,
            ROUND(
                AVG((m.MARKS_OBTAINED / m.MAX_MARKS) * 100), 2
            ) AS AVG_PERCENTAGE
        FROM STUDENT s
        JOIN MARKS m
            ON s.STUDENT_ID = m.STUDENT_ID
        GROUP BY s.DEPARTMENT
        ORDER BY AVG_PERCENTAGE DESC
    """

    try:
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            for row in results:
                print(f"\nDepartment: {row[0]}")
                print(f"Total students with marks: {row[1]}")
                print(f"Average percentage: {row[2]}%")
                print("-" * 40)
        else:
            print("No performance records found.")

    except Exception as error:
        print("Error fetching department summary:", error)

    finally:
        cursor.close()
        connection.close()



def top_students_ranking():
    print("\n--- Top Students Ranking ---")

    connection = get_connection()

    if connection is None:
        print("Unable to connect to database.")
        return

    cursor = connection.cursor()

    query = """
        SELECT
            s.STUDENT_ID,
            s.FIRST_NAME,
            s.LAST_NAME,
            s.DEPARTMENT,
            ROUND(
                AVG((m.MARKS_OBTAINED / m.MAX_MARKS) * 100), 2
            ) AS AVG_PERCENTAGE
        FROM STUDENT s
        JOIN MARKS m
            ON s.STUDENT_ID = m.STUDENT_ID
        GROUP BY
            s.STUDENT_ID,
            s.FIRST_NAME,
            s.LAST_NAME,
            s.DEPARTMENT
        ORDER BY AVG_PERCENTAGE DESC
    """

    try:
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            rank = 1

            for row in results:
                print(f"\nRank: {rank}")
                print(f"Student ID: {row[0]}")
                print(f"Name: {row[1]} {row[2]}")
                print(f"Department: {row[3]}")
                print(f"Average Percentage: {row[4]}%")
                print("-" * 40)

                rank += 1
        else:
            print("No student marks found.")

    except Exception as error:
        print("Error fetching student rankings:", error)

    finally:
        cursor.close()
        connection.close()
