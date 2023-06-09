# Generated by Django 4.1.7 on 2023-03-30 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('date', models.DateTimeField(max_length=100)),
                ('preference', models.CharField(choices=[('morning', 'morning'), ('afternoon', 'afternoon'), ('evening', 'evening')], max_length=10)),
            ],
        ),
    ]
