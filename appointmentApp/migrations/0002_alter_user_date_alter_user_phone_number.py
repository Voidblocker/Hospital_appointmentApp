# Generated by Django 4.1.7 on 2023-03-31 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointmentApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
