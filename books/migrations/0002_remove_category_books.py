# Generated by Django 5.0.4 on 2024-05-07 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='books',
        ),
    ]