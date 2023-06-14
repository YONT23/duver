from django.urls import path, include

urlpatterns = [
    path('inmueble/', include('apps.urls.inmuebles')),
    path('maestra/', include('apps.urls.maestra')),
    path('usuario/', include('apps.urls.usuarios')),
    path('persona/', include('apps.urls.personas')),
    path('auth/', include('apps.urls.auth'))
]