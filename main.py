import psycopg
import os

# connection to the PostgreSQL database
conn = psycopg.connect(
    host = "localhost",
    port = 5432,
    dbname = "student_db",
    user = "postgres",
    password = os.environ["DB_PASSWORD"]
)

cursor = conn.cursor()

# retrieves and displays all students from the database
def getAllStudents(): 
    try:   
        cursor.execute("SELECT * FROM students;")
        students = cursor.fetchall()
        for student in students:
            print(student)
    except psycopg.Error as e:
        # roll back the transaction if a database error occurs
        conn.rollback()
        print("Error retrieving students:", e)

# insert a new student into the database
def addStudent(first_name, last_name, email, enrollment_date):
    try: 
        # use parameterized queries to safely insert the user input
        cursor.execute(
            """
            INSERT INTO students 
            (first_name, last_name, email, enrollment_date) 
            VALUES (%s, %s, %s, %s);
            """,
            (first_name, last_name, email, enrollment_date)
        )

        # commit transaction to save the changes permanently
        conn.commit()
        print("Student added successfully!")
    except psycopg.Error as e:
        conn.rollback()
        print("Error adding student: ", e)

# update the email of a student using their student ID
def updateStudentEmail(student_id, new_email):
    try: 
        cursor.execute(
            "UPDATE students SET email = %s WHERE student_id = %s",
            (new_email, student_id)
        )

        # check whether a student with the specified ID was found
        if cursor.rowcount > 0:
            conn.commit()
            print("Student email updated successfully!")
        else:
            conn.rollback()
            print("No student found with that ID.")
    except psycopg.Error as e:
        conn.rollback()
        print("Error updating student email: ", e)

# delete a student using their student ID
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
        print("Error deleting student: ", e)

# display the menu and process user selections
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
        try:
            input_id = int(input("Enter ID of student: "))
        except ValueError:
            print("Invalid ID. Please enter an integer.")
            continue
        input_new_email = input("Enter new email for student: ")
        updateStudentEmail(input_id, input_new_email)
    elif user_choice == "4":
        try:
            input_delete_id = int(input("Enter ID of student to be deleted: "))
        except ValueError:
            print("Invalid ID. Please enter an integer.")
            continue
        deleteStudent(input_delete_id)
    elif user_choice == "5":
        conn.close()
        break
    else:
        print("Invalid choice. Please enter an integer between 1 and 5.")