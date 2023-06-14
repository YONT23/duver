from django.urls import path
from .views import *

urlpatterns = [
    #Urls Clientes
    path('c', ClienteView.as_view()),
    path('ccreate/', ClienteCreate.as_view()),
    path('cupdate/<int:pk>/', ClienteUpdate.as_view()),
    path('cdelete/<int:pk>/', ClienteDelete.as_view()),
    path('call/', ClienteViewOwner.as_view()),

]