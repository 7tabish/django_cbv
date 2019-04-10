from django.shortcuts import render
from django.views.generic import View  , TemplateView, ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
from myapp.models import students,school
from django.urls import reverse_lazy
class schoolListView(ListView):
    model=school

class schoolDetailView(DetailView):
    #to define userdefine name we use context_objecty_name
    context_object_name = 'school_detail'
    model=school


class schoolCreateView(CreateView):
    fields=('name','location','principal')
    model=school
class schoolupdateView(UpdateView):
    fields=('name','principal')
    model=school
class schoolDeleteView(DeleteView):
    context_object_name = 'school_delete_detail'
    model=school
    success_url = reverse_lazy('list')
class createStudentView(CreateView):
    model=students
    fields=('name','age','school')