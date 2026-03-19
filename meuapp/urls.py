from django.urls import path
from .views import UsuarioListView, UsuarioCreateView, UsuarioUpdateView

urlpatterns = [
    path('listar/', UsuarioListView.as_view(), name='listar_usuarios'),
    path('criar/', UsuarioCreateView.as_view(), name='criar_usuario'),
    path('editar/<int:pk>/', UsuarioUpdateView.as_view(), name='atualizar_usuario'),
    path('deletar/<int:pk>/', UsuarioDeleteView.as_view(), name='deletar_usuario'),
]