from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from uuid import uuid4

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['id'], name='book_id_index')
        ]
        permissions = [
            ('special_status', 'Can read all books')
        ]

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    review = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.review