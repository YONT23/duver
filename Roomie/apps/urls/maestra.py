from django.urls import path
from ..views.maestra import *

urlpatterns = [
    path('', MaestraView.as_view()),
    path('dependencias/', MaestraViewDependencia.as_view()),
    path('create/', MaestraCreate.as_view()),
    path('update/<int:pk>/', MaestraUpdate.as_view()),
    path('delete/<int:pk>/', MaestraDelete.as_view()),
]