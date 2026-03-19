from django.urls import path
from .views import listar_usuarios, criar_usuario, atualizar_usuario, deletar_usuario

urlpatterns = [
    path('listar/', listar_usuarios, name='listar_usuarios'),
    path('criar/', criar_usuario, name='criar_usuario'),
    path('editar/<int:pk>/', atualizar_usuario, name='atualizar_usuario'),
    path('deletar/<int:pk>/', deletar_usuario, name='deletar_usuario'),
]