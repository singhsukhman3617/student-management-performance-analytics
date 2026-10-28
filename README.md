# Student Management & Performance Analytics System

## About the Project

The Student Management & Performance Analytics System is a Python and MySQL-based application designed to manage student records, courses, enrollments, and academic marks. It also provides performance analysis to help identify top-performing students and compare academic performance across departments.

## Features

- Add new student records
- View all students
- Search students by ID
- Add courses
- Enroll students in courses
- Record student marks
- View individual student performance
- Generate department-wise performance summaries
- Rank students based on average marks percentage

## Technologies Used

- **Python** — application logic
- **MySQL** — relational database
- **mysql-connector-python** — Python-to-MySQL connectivity
- **SQL** — data management, joins, and performance analysis

## Project Structure

```text
database/
├── app.py
├── functio.py
├── db.py
├── config.py
├── schema.sql
├── requirements.txt
├── .gitignore
└── README.md
```

## Prerequisites

Before running the project, install:

- Python 3
- MySQL Server
- MySQL Workbench (recommended)
- Visual Studio Code (optional)

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd database
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up the MySQL database

- Open MySQL Workbench and connect to your MySQL server.
- Create your project database.
- Open and execute `schema.sql` in that database.

### 5. Configure the database connection

Update `config.py` with your own MySQL connection details:

- Host
- Username
- Password
- Database name

**Security:** Never publish your database password or other private credentials to GitHub.

### 6. Run the application

```bash
python app.py
```

Follow the menu displayed in the terminal to use the available features.

## Analytics

The application uses SQL queries and aggregate functions to:

- Calculate student performance percentages
- Calculate department-wise average performance
- Rank students by average percentage

## Future Improvements

- Add a graphical user interface
- Improve input validation and error handling
- Add visual charts for academic performance
- Export performance reports to CSV or Excel
- Add secure configuration through environment variables

## Author

Sukhmanpreet Singh Sandhu

Aspiring AI/ML Engineer