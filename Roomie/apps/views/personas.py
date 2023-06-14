from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from ..personas.models import TblPersona
from ..serializers import personaSerializer


class PersonaView(ListAPIView):
    queryset = TblPersona.objects.all()
    serializer_class = personaSerializer

    def get(self, request, *args, **kwargs):
        PersonaData = personaSerializer(self.get_queryset(), many=True)
        return Response(PersonaData.data, status=status.HTTP_200_OK)

class PersonaCreate(CreateAPIView):
    queryset = TblPersona.objects.all()
    serializer_class = personaSerializer

    def post(self, request, *args, **kwargs):
        createData = personaSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonaUpdate(UpdateAPIView):
    queryset = TblPersona.objects.all()
    serializer_class = personaSerializer


class PersonaDelete(DestroyAPIView):
    queryset = TblPersona.objects.all()
    serializer_class = personaSerializer