from django.shortcuts import render

from django.views.generic import CreateView, FormView, ListView, TemplateView
from .models import Category, Project, Task
from .forms import ProjectCreateForm, TaskCreateForm, ProjectTasksListForm

from django.urls import reverse, reverse_lazy


# Create your views here.
def index_view(request):
  return render(request, 'index.html')



class ProjectCreateView(CreateView):
  model= Project
  form_class= ProjectCreateForm
  template_name='todo/project_form.html'
  success_url = reverse_lazy('index')



class TasksProjectList(FormView):
  model= Project
  template_name= 'todo/tasks_project.html'
  form_class= ProjectTasksListForm
  success_url = reverse_lazy('index')

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      # Ajoutez les projets et tâches au contexte
      context['projects'] = Project.objects.all()
      context['tasks'] = Task.objects.all()
      print('##################################')
      for project in Project.objects.all():
        print(project.name)
      print('##################################')
      return context

  def form_valid(self, form):
    selected_project = form.cleaned_data['project']
    tasks_about_selected_project = selected_project.tasks.all()  # Récupère les tâches liées au projet sélectionné
    print(f"Tâches pour {selected_project.name}: {tasks_about_selected_project}")
    context = self.get_context_data(form=form)
    context.update({
        'selected_project': selected_project,
        'tasks_about_selected_project': tasks_about_selected_project,
    })
    return self.render_to_response(context)



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

