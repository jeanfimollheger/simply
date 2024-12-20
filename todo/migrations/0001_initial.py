# Generated by Django 4.2.16 on 2024-12-07 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=225, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=225, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('slug', models.SlugField(blank=True, max_length=225, unique=True)),
                ('target_date', models.DateField()),
                ('done', models.BooleanField(default=False)),
                ('antecedents', models.ManyToManyField(blank=True, related_name='dependents', to='todo.task')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='todo.category')),
                ('projects', models.ManyToManyField(blank=True, related_name='tasks', to='todo.project')),
            ],
        ),
    ]
