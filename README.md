## COMP 3005 Assignment 3 Question 1

Name: Elisa Rispoli

Student Number: 101343589

### Program Description

This program is a Student Management System developed in Python that connects to a PostgreSQL database using the psycopg library. The program allows users to perform four operations on the students table: retrieve and display all students, add a new student, update an existing student's email address, and delete a student. Users can select these operations through a menu-based interface. The program also includes error handling to manage invalid inputs and database errors.

### Building and Running

1. Ensure that Python, PostgreSQL, and the psycopg library are installed.
2. Open pgAdmin and create a PostgreSQL database named student_db.
3. Run the provided SQL script to create the students table and insert the three initial student records.
4. Open PowerShell (Windows) or Terminal (macOS) and navigate to the folder containing the Python application (main.py).
5. Set the PostgreSQL database password as an environment variable by entering:
   - Windows (PowerShell): $env:DB_PASSWORD = "your_postgresql_password"
   - macOS: export DB_PASSWORD="your_postgresql_password" 
7. Run the application by entering:
   - Windows: python main.py
   - macOS: python3 main.py
9. To use the program:
   - Enter 1 to retrieve and display all students
   - Enter 2 to add a student by providing their first and last name, email, and enrollment date
   - Enter 3 to update a student's email address using their student ID
   - Enter 4 to delete a student using their student ID
   - Enter 5 to exit the program

### Video Demonstration
