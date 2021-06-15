from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Snack
# Create your views here.

class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack

class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack
    
class SnackUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = ["title", "purchaser", "description"]

class SnackCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = ["title", "purchaser", "description"]

class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    success_url = reverse_lazy("snack_list")


