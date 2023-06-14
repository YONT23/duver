from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import usuarioSerializer, personaSerializer
from django.contrib.auth.models import User

class UsuarioView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = usuarioSerializer

    def get(self, request, *args, **kwargs):
        UsuarioData = usuarioSerializer(self.get_queryset(), many=True)
        return Response(UsuarioData.data, status=status.HTTP_200_OK)

class UsuarioUpdate(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = usuarioSerializer

class UsuarioDelete(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = usuarioSerializer