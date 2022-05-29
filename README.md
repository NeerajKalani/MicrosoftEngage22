# MicrosoftEngage22

# Facial Recognition System

A facial recognition project which recognizes a student's face and saves the attendance in database.

It also can create a report on attendance and save that pdf.

It can also be a student management software and show all students with their info and attendance with a dashboard.

# Presentation Video Link

https://drive.google.com/drive/folders/1D1jK9sOiy00rzxYAMqjre7yX1zc4rWEk

# Basic Functionality

    1. Capturing Images, Training Model and Recognising Face.
    2. Dashboard That shows all students present as well as absent and a user can view and delete the student using dashboard.
    3. It creates a excel sheets which adds the unique students.

# Technical Aspect

Frontend

    HTML
    CSS
    BOOTSTRAP

Backend

    Python ( backend programming language )
    Django (web development framework)
    OpenCV ( Computer Vision Library )

# Installation

Kindly run the commands in anaconda.
The Code is written in Python . To install the required packages and libraries, run this command in the project directory after cloning the repository:-

    pip install -r requirements.txt

Alternative(Try these commands)

    pip install numpy
    pip install opencv-contrib-python
    pip install opencv-python
    pip install pandas
    pip install Pillow
    pip install python-dateutil
    pip install pytz
    pip install six
    pip install sqlparse
    
After cloning check that all the libraries are installed .

For running the same project go to the project folder where the manage.py file is located and run the following command into the command prompt:-
    
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser 
    python manage.py runserver

# Directory Tree

    ├── face_recognition_system (application folder)
    │   ├── face_rec
    |       ├── migrations
    |       ├── templates (html files are stored here)
    |       ├── admin.py (admin related data is stored here)
    |       ├── apps.py (information related to this application is stored here)
    |       ├── models.py (database information is stored here)
    |       ├── urls.py (urls related to this project are stored here)
    |       └── views.py (the working of each url is stored in a view)
    │   ├── face_recognition_system (project folder)
    │       ├── asgi.py
    |       ├── settings.py (main file where all the information is stored)
    |       ├── urls.py (urls are redirected to urls file of application)
    |       └── wsgi.py (this file is used to run the project when deploying)
    |   ├── requirements.txt
    |   ├── Procfile (it contains info on how to run the application when deployed)
    |   ├── README.md (markdown file or documentation of this project)
    |   └── manage.py (this file is used to run the project on client side)

