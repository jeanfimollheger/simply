from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category (models.Model):
  name= models.CharField(max_length=225, unique=True)
  slug= models.SlugField(max_length=225, unique=True, blank=True)
  
  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug= slugify(self.name)
    super().save(*args, **kwargs)

  def __str__(self):
    return self.slug


class Project (models.Model):
  name= models.CharField(max_length=225, unique=True)
  slug= models.SlugField(max_length=225, unique=True, blank=True)
  
  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug= slugify(self.name)
    super().save(*args, **kwargs)

  def __str__(self):
    return self.slug


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