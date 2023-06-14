from django.urls import path
from ..views.personas import *

urlpatterns = [
    path('', PersonaView.as_view()),
    path('create/', PersonaCreate.as_view()),
    path('update/<int:pk>/', PersonaUpdate.as_view()),
    path('delete/<int:pk>/', PersonaDelete.as_view()),
]