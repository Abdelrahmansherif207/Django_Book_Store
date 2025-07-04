from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_title_length(value):
    if not (10 <= len(value) <= 50):
        raise ValidationError('Book title must be between 10 and 50 characters.')

def validate_category_name(value):
    if len(value) < 2:
        raise ValidationError('Category name must be at least 2 characters.')

class Category(models.Model):
    name = models.CharField(max_length=50, validators=[validate_category_name])

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50, validators=[validate_title_length])
    desc = models.TextField()
    rate = models.DecimalField(max_digits=3, decimal_places=1)
    views = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

class ISBN(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    author_title = models.CharField(max_length=100)
    book_title = models.CharField(max_length=100)
    isbn_number = models.CharField(max_length=13, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.isbn_number:
            import uuid
            self.isbn_number = str(uuid.uuid4().int)[:13]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.isbn_number
