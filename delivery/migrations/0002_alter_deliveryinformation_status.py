# Generated by Django 5.0.4 on 2024-05-15 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryinformation',
            name='status',
            field=models.CharField(choices=[('PREPARING', 'Preparing'), ('IN_TRANSIT', 'In transit'), ('ARRIVED', 'Arrived'), ('DELIVERING', 'DELIVERING'), ('DELIVERED', 'Delivered')], default='PREPARING', max_length=20),
        ),
    ]
