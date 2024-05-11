from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publisher = models.CharField(max_length=100)
    edition = models.IntegerField()
    be_sold = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    cover = models.ImageField(upload_to='books/', null=True, blank=True)
    tags = models.ManyToManyField(Category, related_name='tags')

    def __str__(self):
        return self.title

    # def add_tag(self, tag):
    #     self.tags.add(tag)
    #     self.save()
