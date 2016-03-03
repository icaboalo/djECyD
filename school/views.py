from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy #para regresar a otra url
from django.views.generic import ListView, DetailView, TemplateView #vistas para lista y detalle
from django.views.generic.edit import CreateView, UpdateView, DeleteView #vistas para modificar
from .models import School #importamos el modelo

fieldList = ['name']

# Create your views here.
class Index(TemplateView):
	template_name = 'index.html'

class SchoolListView(ListView):
	model = School
	template_name = "school/school_index.html"

class SchoolDetail(DetailView):
	model = School
	def get_context_data(self, **kwargs):
	    context = super(SchoolDetail, self).get_context_data(**kwargs)
	    return context #aqui regresa el resultado de la tienda solicitada

class SchoolCreate(CreateView):
	model = School
	fields = fieldList
	success_url = reverse_lazy('school_index')

class SchoolUpdate(UpdateView):
	model = School
	fields = fieldList
	success_url = reverse_lazy('school_index')

class SchoolDelete(DeleteView):
	model = School
	success_url = reverse_lazy('school_index')