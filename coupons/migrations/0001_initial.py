# Generated by Django 5.0.4 on 2024-05-07 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.CharField(max_length=20)),
                ('usage_limit', models.IntegerField()),
                ('is_expired', models.BooleanField(default=False)),
                ('minimum_order_value', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]