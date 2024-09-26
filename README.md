# NOTES-APP-USING-FASTAPI-MONGODB
A simple Notes App developed using FastAPI, MongoDB (PyMongo), Pydantic for data validation, and Jinja2 templates for rendering HTML pages.

# Features
Create Notes: Add new notes with a title and description.
View Notes: View all saved notes in a structured layout.
Update Notes: Edit existing notes.
Delete Notes: Remove notes you no longer need.

# Tech Stack
Backend: FastAPI
Database: MongoDB using PyMongo
Validation: Pydantic
Frontend: HTML rendered using Jinja2 templates
# Installation
Clone the repository:
git clone [https://github.com/your-username/notes-app.git](https://github.com/Deepusain/NOTES-APP-USING-FASTAPI-MONGODB)

Navigate to the project directory:
cd notes-app

Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate  # For Windows

Install dependencies:
pip install -r requirements.txt

Run the FastAPI server:
uvicorn app.main:app --reload

Visit http://127.0.0.1:8000 to access the Notes App.

# Usage
Home Page: Displays a list of all notes.
Add Note: Click on the "Add Note" button to create a new note.
Edit Note: Click on the "Edit" button beside each note to modify it.
Delete Note: Click on the "Delete" button to remove a note.

# Project Structure
.
├── app
│   ├── __init__.py
│   ├── main.py                # Entry point for FastAPI application
│   ├── models.py              # Pydantic models for data validation
│   ├── routes.py              # Routes for handling requests
│   └── templates              # Jinja2 HTML templates
│       ├── base.html
│       ├── index.html
│       └── note_form.html
├── .env                       # Environment variables
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation

# Requirements
Python 3.x
MongoDB

# License
This project is licensed under the MIT License.
