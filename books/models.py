from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publisher = models.CharField(max_length=100)
    edition = models.IntegerField()
    be_sold = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    # cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    tags = models.ManyToManyField(Category, related_name='tags')

    def __str__(self):
        return self.title



