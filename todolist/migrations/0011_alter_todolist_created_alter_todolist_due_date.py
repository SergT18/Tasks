# Generated by Django 4.2 on 2024-12-03 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0010_auto_20210723_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='2024-12-03'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default='2024-12-03'),
        ),
    ]