from .models import Usuario
from django.views.generic.edit import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy    
from .forms import UsuarioForm

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'form.html'
    success_url = reverse_lazy('listar_usuarios') 

class UsuarioListView(ListView):
    model = Usuario
    template_name = 'list.html'
    context_object_name = 'usuarios'

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'form.html'
    success_url = reverse_lazy('listar_usuarios')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'confirmar_delete.html'
    success_url = reverse_lazy('listar_usuarios')