# Generated by Django 3.1.13 on 2021-08-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20210802_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='categories',
            field=models.ManyToManyField(related_name='tasks', to='todo.Category'),
        ),
    ]