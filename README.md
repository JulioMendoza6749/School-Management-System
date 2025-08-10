## School Management System

# Description
This is a local School Management System developed in Python with a graphical interface using Tkinter.
The system manages student data and academic records, storing the information in a MySQL database.

The database is loaded locally using the provided control_escolar.sql file, which should be imported into a local MySQL server (e.g., via phpMyAdmin).

# Technologies and Dependencies
- Python 3.x
- mysql-connector-python — to connect with MySQL
- json (built-in Python module) — for JSON parsing
- re (built-in Python module) — for regular expressions
- Tkinter — for the graphical user interface

# Installation
1-  Clone the repository:
git clone https://github.com/JulioMendoza6749/School-Management-System.git

2- Import the control_escolar.sql file into your local MySQL database using phpMyAdmin or the MySQL command line.

3- Install required Python packages:
pip install mysql-connector-python tkcalendar

4- Run the main application: 
python App.py

# Usage
The main application file is App.py.
For testing or demonstration purposes, the login line is commented out, allowing access to the system without verifying users in the database.
To enable user authentication, uncomment the login line in App.py.

# Collaborators
This project was developed collaboratively by:
- Gael Emiliano Anaya García
- Julio Alejandro Mendoza Bernardo
- Diego Levy Absalón Navarro Hernández

# License
This project is licensed under the MIT License - see the LICENSE file for details.
