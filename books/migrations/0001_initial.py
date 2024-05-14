# Generated by Django 5.0.4 on 2024-05-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('publisher', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
                ('edition', models.IntegerField()),
                ('pages_num', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='books/')),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('tags', models.ManyToManyField(related_name='tags', to='books.category')),
            ],
        ),
    ]
