Fitness Tracker API

A Django REST Framework API for managing fitness activities.
Users can register, log in, and track workouts such as running, cycling, swimming, or weightlifting.
The API also provides activity summaries and metrics over time.

📌 Features

👤 User Management: Register, login (JWT), and manage your account

🏋️ Activity Management (CRUD): Log, view, update, and delete activities

📖 Activity History: View all logged activities with filters by date and type

📊 Metrics & Reports: Summaries of duration, calories, and distance over time

🔒 Authentication: JWT-based secure access

⚡ Deployed on PythonAnywhere

🚀 Live Demo

Base URL:

https://pricharddube.pythonanywhere.com/api/user/

🛠️ Installation (local setup)
# clone the repo
git clone https://github.com/YOUR-USERNAME/fitness_tracker.git
cd fitness_tracker

# create virtualenv
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# install dependencies
pip install -r requirements.txt

# run migrations
python manage.py migrate

# create superuser
python manage.py createsuperuser

# start server
python manage.py runserver

🔑 Authentication

Register: POST /api/users/register/

Login (JWT): POST /api/token/

Use the access token in headers:

Authorization: Bearer <your_token>

📚 API Endpoints
👤 Users
Method	Endpoint	Description
POST	/api/users/register/	Register a new user
POST	/api/token/	Login (get JWT token)
POST	/api/token/refresh/	Refresh token
🏋️ Activities
Method	Endpoint	Description
GET	/api/activities/	List user’s activities (with pagination, filtering, sorting)
POST	/api/activities/	Create a new activity
GET	/api/activities/{id}/	Retrieve a specific activity
PUT	/api/activities/{id}/	Update an activity
DELETE	/api/activities/{id}/	Delete an activity

Activity JSON Example

{
  "activity_type": "Running",
  "duration_min": 30,
  "distance_km": 5.0,
  "calories": 300,
  "date": "2025-08-28",
  "notes": "Morning run"
}

📊 Metrics
Method	Endpoint	Description
GET	/api/metrics/	Get activity summary (totals & trends)

Example
GET /api/metrics/?date_after=2025-08-01&date_before=2025-08-28&group_by=week

📝 Example Workflow

Register: POST /api/users/register/

Login: POST /api/token/ → copy access token

Create activity: POST /api/activities/ with JSON body

List activities: GET /api/activities/

Metrics: GET /api/metrics/?group_by=month

👨‍💻 Tech Stack

Python 3.10

Django 5+

Django REST Framework

Simple JWT (Authentication)

SQLite (local), MySQL/Postgres (deploy)

PythonAnywhere (deployment)
