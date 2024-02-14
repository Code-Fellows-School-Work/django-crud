from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.shortcuts import render
from .models import Snack
from django.urls import reverse_lazy

class AboutPageView(TemplateView):
    template_name = 'about.html'

class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack
    context_object_name = 'snacks'

class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack

class SnackCreateView(CreateView):
    template_name = 'snack_create.html'
    model = Snack
    fields = '__all__'

class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    model = Snack
    field = '__all__'

class SnackUpdateView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snack
    success_url = reverse_lazy('snack_list')
