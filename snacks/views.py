from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
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
    fields = '__all__'

class SnackDeleteView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snack
    success_url = reverse_lazy('snack_list')

def about_me(request):
    context = {
        'image_url': '.assets/PXL_20230816_231329155.MP.jpg',
    }
    return render(request, 'about_me.html', context)
