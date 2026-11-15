import psycopg

conn = psycopg.connect(
    host = "localhost",
    port = 5432,
    dbname = "student_db",
    user = "postgres",
    password = "lisa"
)

print("Connected to PostgreSQL successfully!")

cursor = conn.cursor()

def getAllStudents():    
    cursor.execute("SELECT * FROM students;")
    students = cursor.fetchall()
    for student  in students:
        print(student)

def addStudent(first_name, last_name, email, enrollment_date):
    try: 
        cursor.execute(
            """
            INSERT INTO students 
            (first_name, last_name, email, enrollment_date) 
            VALUES (%s, %s, %s, %s);
            """,
            (first_name, last_name, email, enrollment_date)
        )
        conn.commit()
        print("Student added successfully!")
    except psycopg.Error as e:
        conn.rollback()
        print("Error adding student: ", e)

def updateStudentEmail(student_id, new_email):
    try: 
        cursor.execute(
            "UPDATE students SET email = %s WHERE student_id = %s",
            (new_email, student_id)
        )

        if cursor.rowcount > 0:
            conn.commit()
            print("Student email updated successfully!")
        else:
            conn.rollback()
            print("No student found with that ID.")
    except psycopg.Error as e:
        conn.rollback()
        print("Error updating student email: ", e)

def deleteStudent(student_id):
    try:
        cursor.execute(
            "DELETE FROM students WHERE student_id = %s",
            (student_id,)
        )
        conn.commit()
        if cursor.rowcount > 0:
            print("Student deleted successfully!")
        else:
            print("No student found with that ID.")
    except psycopg.Error as e:
        conn.rollback()
        print("Error updating student email: ", e)


while True:
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. View all students")
    print("2. Add a student")
    print("3. Update a student's email")
    print("4. Delete a student")
    print("5. Exit\n")

    user_choice = input("Enter your choice (1-5): ")

    if user_choice == "1":
        getAllStudents()
    elif user_choice == "2":
        input_first_name = input("Enter student first name: ")
        input_last_name = input("Enter student last name: ")
        input_email = input("Enter student email: ")
        input_date = input("Enter date of enrollment of student (YYYY-MM-DD): ")
        addStudent(input_first_name, input_last_name, input_email, input_date)
    elif user_choice == "3":
        input_id = int(input("Enter ID of student: "))
        input_new_email = input("Enter new email for student: ")
        updateStudentEmail(input_id, input_new_email)
    elif user_choice == "4":
        input_delete_id = int(input("Enter ID of student to be deleted: "))
        deleteStudent(input_delete_id)
    elif user_choice == "5":
        conn.close()
        break
    else:
        print("Invalid choice. Please enter an integer between 1 and 5.")