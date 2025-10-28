Student API – Django REST Framework

A simple Django REST Framework (DRF) project to manage student data.
This API allows users to add, view, and filter student records, including a special endpoint to fetch adult students (age > 18).

Features:
Create new student records
Retrieve all students
Filter students older than 18
REST API built using Django REST Framework

Tech Stack:
Python 3.11+
Django 5.2
Django REST Framework 3.16
SQLite (default Django database)

Project Structure
student_api_project/
│
├── core/
│   ├── core/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   ├── students/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── ...
│   ├── manage.py
│
├── venv/
└── requirements.txt

Endpoints working

Test in browser:
1.List/Create Students:
http://127.0.0.1:8000/api/students/

2.Adult Students:
http://127.0.0.1:8000/api/students/adults/

3.Try a sample POST:
{
  "name": "Sujata",
  "age": 21,
  "email": "sujata@example.com"
}



