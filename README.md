# ET721_lab_feedback2
This is a simple feedback system built with Django. Users can submit feedback for specific items (e.g., products or articles), including a rating and a comment. The system displays average ratings and lists feedback for each item.

## Features
- Users can view items and their feedback.
- Feedback includes a rating (1-5) and a comment.
- Average rating is displayed on the item detail page.
- Admin can add items and feedback via the Django admin panel.

## Setup and Installation

## Create and activate a virtual environment
```bash
python3 -m venv myvirtual
source myVirtual/bin/activate  # On Windows, use `venv\Scripts\activate`
```
##Install Django
Within the activated virtual environment, install Django.
```bash
pip install django
```
## Create a new Django project: Create a project named feedbackproject.
```bash
django-admin startproject feedbackproject .
cd feedbackproject
```
## Create a Django app called feedback
Inside the feedbackproject directory, create the app.
```bash
python manage.py startapp feedback
```
## Configure settings
Open feedbackproject/settings.py
Add feedback to the INSTALLED_APPS list:
```pyton
INSTALLED_APPS = [
    # Other apps...
    'feedback',
]
```
## Run server test
Verify that the project is set up correctly by running the Django development server.
```bash
python manage.py runserver
```

```bash
git clone https://github.com/yourusername/ET721_lab_feedback.git
cd ET721_lab_feedback
