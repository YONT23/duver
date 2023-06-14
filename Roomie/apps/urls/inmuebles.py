from django.urls import path
from ..views.inmuebles import *
from ..views.consultas import *

urlpatterns = [
    path('', InmuebleView.as_view()),
    path('create/', InmuebleCreate.as_view()),
    path('update/<int:pk>/', InmuebleUpdate.as_view()),
    path('delete/<int:pk>/', InmuebleDelete.as_view()),
    path('all/', InmuebleViewOwner.as_view()),
    ####### Consultas #######
    path('consulta1/', Consulta1.as_view()),
    path('consulta2/', Consulta2.as_view()),
    path('consulta3/', Consulta3.as_view()),
    path('consulta4/', Consulta4.as_view()),
    path('consulta5/', Consulta5.as_view()),
    path('consulta6/', Consulta6.as_view()),
]