from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from apps.personas.models import *
from apps.serializers import *

##Cliente CRUD

class ClienteView(ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get(self, request, *args, **kwargs):
        clienteData = ClienteSerializer(self.get_queryset(), many=True)
        return Response(clienteData.data, status=status.HTTP_200_OK)

class ClienteViewOwner(ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get(self, request, *args, **kwargs):
        clienteData = ClienteSerializer(self.get_queryset(), many=True)
        return Response(clienteData.data, status=status.HTTP_200_OK)

class ClienteCreate(CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def post(self, request, *args, **kwargs):
        createData = ClienteSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class ClienteUpdate(UpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDelete(DestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
