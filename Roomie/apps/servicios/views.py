from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from apps.servicios.models import *
from apps.serializers import *

##Disponibilidad CRUD

class DisponibilidadView(ListAPIView):
    queryset = Disponibilidad.objects.all()
    serializer_class = DisponibilidadSerializer

    def get(self, request, *args, **kwargs):
        dispoData = DisponibilidadSerializer(self.get_queryset(), many=True)
        return Response(dispoData.data, status=status.HTTP_200_OK)

class DisponibilidadViewOwner(ListAPIView):
    queryset = Disponibilidad.objects.all()
    serializer_class = DisponibilidadSerializer

    def get(self, request, *args, **kwargs):
        ServicioData = DisponibilidadSerializer(self.get_queryset(), many=True)
        return Response(ServicioData.data, status=status.HTTP_200_OK)

class DisponibilidadCreate(CreateAPIView):
    queryset = Disponibilidad.objects.all()
    serializer_class = DisponibilidadSerializer

    def post(self, request, *args, **kwargs):
        createData = DisponibilidadSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class DisponibilidadUpdate(UpdateAPIView):
    queryset = Disponibilidad.objects.all()
    serializer_class = DisponibilidadSerializer

class DisponibilidadDelete(DestroyAPIView):
    queryset = Disponibilidad.objects.all()
    serializer_class = DisponibilidadSerializer
