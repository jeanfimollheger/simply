# Generated by Django 4.2.16 on 2024-12-08 12:57

from django.db import migrations, models
import todo.models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='target_project_date',
            field=models.DateField(default=todo.models.get_default_target_date),
        ),
    ]
