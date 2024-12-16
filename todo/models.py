from django.db import models
from django.utils.text import slugify
from datetime import date, timedelta

# fonctions à disposition
def get_default_target_date():
  date.today() + timedelta(days=45)


# Create your models here.
class Category (models.Model):
  name= models.CharField(max_length=225, unique=True)
  slug= models.SlugField(max_length=225, unique=True, blank=True)
  
  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug= slugify(self.name)
    super().save(*args, **kwargs)

  def __str__(self):
    return f"{self.id} - {self.slug}"


class Project (models.Model):
  name= models.CharField(max_length=225, unique=True)
  slug= models.SlugField(max_length=225, unique=True, blank=True)
  target_project_date= models.DateField(default=get_default_target_date)
  
  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug= slugify(self.name)
    super().save(*args, **kwargs)

  def __str__(self):
    return f"{self.id} - {self.slug}"

class Task (models.Model):
  name= models.CharField(max_length=225)
  slug= models.SlugField(max_length=225, unique=True, blank=True)
  target_date= models.DateField()
  done= models.BooleanField(default=False)
  category= models.ForeignKey(Category, on_delete=models.CASCADE, related_name="tasks", null=True, blank=True)
  projects= models.ManyToManyField(Project, related_name='tasks', blank=True)
  antecedents =models.ManyToManyField('self', related_name='dependents', symmetrical=False, blank=True)

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug= slugify(self.name)
    super().save(*args, **kwargs)

  def __str__(self):
    return self.slug