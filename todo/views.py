from django.shortcuts import render

from django.views.generic import CreateView
from .models import Project
from .forms import ProjectCreateForm

from django.urls import reverse, reverse_lazy


# Create your views here.
def index_view(request):
  return render(request, 'index.html')


class ProjectCreateView(CreateView):
  model= Project
  form_class= ProjectCreateForm
  template_name='todo/project_form.html'