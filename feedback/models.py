from django.db import models

# Model for Item (e.g., Product or Article)
class Item(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Model for Feedback
class Feedback(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='feedbacks')
    comment = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback for {self.item.name} - Rating: {self.rating}'

