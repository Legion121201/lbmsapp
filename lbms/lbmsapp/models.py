from django.db import models

class Book(models.Model):
    CATEGORY_CHOICES = [
        ('Sci-Fi', 'Sci-Fi'),
        ('Fiction', 'Fiction'),
        ('Comedy', 'Comedy'),
    ]
    
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    
    def __str__(self):
        return self.title
    
    class Meta:
        app_label = 'lbmsapp'

class User(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    college = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=10)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.user.name} on {self.order_date}"
