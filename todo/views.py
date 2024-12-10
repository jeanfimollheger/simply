from django.shortcuts import render

from django.views.generic import CreateView, FormView, TemplateView
from .models import Category, Project, Task
from .forms import ProjectCreateForm, TaskCreateForm

from django.urls import reverse, reverse_lazy


# Create your views here.
def index_view(request):
  return render(request, 'index.html')


class ProjectCreateView(CreateView):
  model= Project
  form_class= ProjectCreateForm
  template_name='todo/project_form.html'
  success_url = reverse_lazy('index')

class TaskCreateView(FormView):
  template_name='todo/combined_task_form.html'
  form_class=TaskCreateForm
  success_url = reverse_lazy('index')

  def form_valid(self, form):
        # Sauvegarde le formulaire
        form.save()
        return super().form_valid(form)
  
  def get_context_data(self, **kwargs):
    context=super().get_context_data(**kwargs)
    context['categories_list']=Category.objects.all()
    context['projects_list']=Project.objects.all()
    context['tasks_list']=Task.objects.all()
    return context

