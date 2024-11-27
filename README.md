# ET721_lab_feedback2
This is a simple feedback system built with Django. Users can submit feedback for specific items (e.g., products or articles), including a rating and a comment. The system displays average ratings and lists feedback for each item.

## Features
- Users can view items and their feedback.
- Feedback includes a rating (1-5) and a comment.
- Average rating is displayed on the item detail page.
- Admin can add items and feedback via the Django admin panel.

## Create and activate a virtual environment
```bash
python3 -m venv myvirtual
source myVirtual/bin/activate
```
## Install Django
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

## Define the Model 
Define the **Item** and **Feedback** models: Open **feedback/models.py** and define the models.
```python
from django.db import models

class Item(models.Model):
    # Define fields for the Item model here
    # Example: name = models.CharField(max_length=100)
    
    def __str__(self):
        # Return a string representation of the item
        pass


class Feedback(models.Model):
    # Define fields for the Feedback model here
    # Example: item = models.ForeignKey(Item, on_delete=models.CASCADE)
    
    def __str__(self):
        # Return a string representation of the feedback
        pass
```
## Run migrations
Create and apply migrations to update the database schema.
```bash
python manage.py makemigrations
python manage.py migrate
```
## Create Forms
Create a form for feedback submission: In **feedback/forms.py**, create the **FeedbackForm** to handle feedback submission.
```python
from django import forms
# Import the model for which the form is being created
# Example: from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback  # Specify the model the form is based on
        fields = []  # Define the list of fields to be included in the form

    def clean_rating(self):
        # Implement custom validation for the rating field here
        # Example: Get the rating from cleaned_data and perform validation
        pass
```
## Develop Views
Create views for displaying item details and handling feedback: Open feedback/views.py and define the necessary views.
```python
from django.shortcuts import render, get_object_or_404, redirect
# Import the necessary models and forms here
# Example: from .models import Item, Feedback
# Example: from .forms import FeedbackForm

def item_detail(request, item_id):
    # Get the item object based on the item_id
    item = get_object_or_404(Item, id=item_id)
    
    # Retrieve feedbacks related to this item (adjust if needed)
    feedbacks = item.feedbacks.all()

    # Calculate the average rating of the feedbacks
    # Example: average_rating = feedbacks.aggregate(models.Avg('rating'))['rating__avg'] or 0
    average_rating = 0  # Update this as per your logic

    # Initialize the form for feedback submission
    form = FeedbackForm(request.POST or None)

    if form.is_valid():
        # Save the form data, but do not commit it yet
        feedback = form.save(commit=False)
        
        # Link the feedback to the current item
        feedback.item = item
        
        # Save the feedback object
        feedback.save()

        # Redirect to the same item detail page after saving the feedback
        return redirect('item_detail', item_id=item.id)

    # Context for rendering the template
    context = {
        'item': item,
        'feedbacks': feedbacks,
        'average_rating': average_rating,
        'form': form,
    }

    # Render the item detail page with feedbacks and the form
    return render(request, 'feedback/item_detail.html', context)
```
## Design Templates
Create a template to display the item and its feedback: Create the item_detail.html template in **feedback/templates/feedback/**.

```HTML
<!DOCTYPE html>
<html>
<head>
    <title>{{ item.name }} - Feedback</title>
</head>
<body>
    <h1>{{ item.name }}</h1>
    <p>Average Rating: {{ average_rating|floatformat:1 }}</p>

    <h2>Feedback</h2>
    {% for feedback in feedbacks %}
        <!-- Display each feedback's rating and comment -->
        <p><strong>{{ feedback.rating }} / 5</strong> - {{ feedback.comment }}</p>
    {% empty %}
        <!-- Message when no feedback exists -->
        <p>No feedback yet.</p>
    {% endfor %}

    <h3>Submit Feedback</h3>
    <form method="post">
        {% csrf_token %}
        <!-- Render the form fields (e.g., comment, rating) -->
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
## Configure URLs
Define URL patterns for views: Open **feedback/urls.py** and define the necessary URL patterns.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
]
```
In **feedbackproject/urls.py**, include the feedback app URLs:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('feedback.urls')),
]
```

```bash
git clone https://github.com/yourusername/ET721_lab_feedback.git
cd ET721_lab_feedback
