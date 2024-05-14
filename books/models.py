from django.db import models
from django.middleware import locale
from django.utils.text import slugify
from unidecode import unidecode


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Book(models.Model):
    # Attributes
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publisher = models.CharField(max_length=100)
    pub_date = models.DateField()
    pages_num = models.IntegerField()
    is_available = models.BooleanField(default=True)
    cover = models.ImageField(upload_to='books/', null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=False, blank=True, editable=True)

    # Relationships
    tags = models.ManyToManyField(Category, related_name='tags')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            unidecode_slug = unidecode(self.title + " " + self.author).lower()
            self.slug = slugify(unidecode_slug, {locale: 'vi'})
        super().save(*args, **kwargs)

    # def add_tag(self, tag):
    #     self.tags.add(tag)
    #     self.save()
