from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Feedback
from .forms import FeedbackForm
from django.db import models


def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    feedbacks = item.feedbacks.all()
    form = FeedbackForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        feedback = form.save(commit=False)
        feedback.item = item
        feedback.save()
        return redirect('item_detail', item_id=item.id)
    
    average_rating = feedbacks.aggregate(models.Avg('rating'))['rating__avg'] or 0

    return render(request, 'feedback/item_detail.html', {
        'item': item,
        'feedbacks': feedbacks,
        'form': form,
        'average_rating': average_rating,
    })

def home(request):
    items = Item.objects.all()
    return render(request, 'feedback/home.html', {'items': items})

