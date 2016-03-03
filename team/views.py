from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy #para regresar a otra url
from django.views.generic import ListView, DetailView, TemplateView #vistas para lista y detalle
from django.views.generic.edit import CreateView, UpdateView, DeleteView #vistas para modificar
from .models import * #importamos el modelo

teamFieldList = ['name', 'grade', 'school', 'leader', 'user']
kidFieldList = ['name', 'last_name', 'team']
leaderFieldList = ['name', 'last_name', 'grade', 'school']

# Create your views here.

#Team Views
class TeamListView(ListView):
	model = Team
	template_name = 'team/team_index.html'

class TeamDetail(DetailView):
	model = Team
	def get_context_data(self, **kwargs):
	    context = super(TeamDetail, self).get_context_data(**kwargs)
	    return context

class TeamCreate(CreateView):
	model = Team
	fields = teamFieldList
	success_url = reverse_lazy('team_index')

class TeamUpdate(UpdateView):
	model = Team
	fields = teamFieldList
	success_url = reverse_lazy('team_index')

class TeamDelete(DeleteView):
    model = Team
    success_url = reverse_lazy('team_index')

#Kid Views
class KidListView(ListView):
    model = Kid
    template_name = "kid/kid_index.html"

class KidDetail(DetailView):
    model = Kid
    template_name = 'kid/kid_detail.html'
    def get_context_data(self, **kwargs):
        context = super(KidDetail, self).get_context_data(**kwargs)
        return context

class KidCreate(CreateView):
    model = Kid
    template_name = 'kid/kid_form.html'
    fields = kidFieldList
    success_url = reverse_lazy('kid_index')

class KidUpdate(UpdateView):
    model = Kid
    template_name = 'kid/kid_update.html'
    fields = kidFieldList
    success_url = reverse_lazy('kid_index')

class KidDelete(DeleteView):
    model = Kid
    template_name = 'kid/kid_confirm_delete.html'
    success_url = reverse_lazy('kid_index')

#Leader Views
class LeaderListView(ListView):
    model = Leader
    template_name = "leader/leader_index.html"

class LeaderDetail(DetailView):
    model = Leader
    template_name = "leader/leader_detail.html"
    def get_context_data(self, **kwargs):
        context = super(LeaderDetail, self).get_context_data(**kwargs)
        return context

class LeaderCreate(CreateView):
    model = Leader
    template_name = "leader/leader_form.html"
    fields = leaderFieldList
    success_url = reverse_lazy('leader_index')

class LeaderUpdate(UpdateView):
    model = Leader
    template_name = "leader/leader_update.html"
    fields = leaderFieldList
    success_url = reverse_lazy('leader_index')

class LeaderDelete(DeleteView):
    model = Leader
    template_name = "leader/leader_confirm_delete.html"    
    success_url = reverse_lazy('leader_index')