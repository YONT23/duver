from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from ..servicios.models import TblInmueble
from ..serializers import inmuebleSerializer,inmuebleDetailSerializer


class InmuebleView(ListAPIView):
    queryset = TblInmueble.objects.all()
    serializer_class = inmuebleSerializer

  #  def get_queryset(self):
  #      query = self.request.GET['search']
  #      if not bool(query):
  #          return TblInmueble.objects.all()
  #      return TblInmueble.objects.filter(descripcion=query)

    def get(self, request, *args, **kwargs):
        inmuebleData = inmuebleDetailSerializer(self.get_queryset(), many=True)
        return Response(inmuebleData.data, status=status.HTTP_200_OK)


class InmuebleViewOwner(ListAPIView):
    queryset = TblInmueble.objects.all()
    serializer_class = inmuebleSerializer

    def get_queryset(self):
        return TblInmueble.objects.filter(dueño__id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        inmuebleData = inmuebleSerializer(self.get_queryset(), many=True)
        return Response(inmuebleData.data, status=status.HTTP_200_OK)


class InmuebleCreate(CreateAPIView):
    queryset = TblInmueble.objects.all()
    serializer_class = inmuebleSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        inmueble = request.data
        inmueble['dueño'] = request.user.id
        inmueble['pais_id'] = request.data['pais']
        createData = inmuebleSerializer(data=inmueble)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)


class InmuebleUpdate(UpdateAPIView):
    queryset = TblInmueble.objects.all()
    serializer_class = inmuebleSerializer


class InmuebleDelete(DestroyAPIView):
    queryset = TblInmueble.objects.all()
    serializer_class = inmuebleSerializer