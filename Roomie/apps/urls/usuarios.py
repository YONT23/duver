from django.urls import path
from ..views.usuarios import *

urlpatterns = [
    path('', UsuarioView.as_view()),
    path('update/<int:pk>/', UsuarioUpdate.as_view()),
    path('delete/<int:pk>/', UsuarioDelete.as_view()),
]