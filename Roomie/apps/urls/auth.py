from django.urls import path
from ..views.auth import *

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', UsuarioCreate.as_view())
]