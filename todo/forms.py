from django import forms
from .models import Project, Task

class ProjectCreateForm(forms.ModelForm):
  class Meta:
    model= Project
    fields = ['name', 'target_project_date']


class TaskCreateForm(forms.ModelForm):
  class Meta:
    model= Task
    fields = ['name', 'target_date', 'category', 'projects', 'antecedents']
    labels = {'name':'nom', 'target_date':'date cible', 'category':'catégorie', 'projects':'projet(s)', 'antecedents':'antécédent(s)'}
    widgets = {'category': forms.RadioSelect(), 'projects':forms.CheckboxSelectMultiple(), 'antecedents':forms.CheckboxSelectMultiple}