from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from ..personas.models import *
from ..serializers import maestraSerializer

class MaestraView(ListAPIView):
    queryset = TblMaestra.objects.all()
    serializer_class = maestraSerializer

    def get(self, request, *args, **kwargs):
        MaestraData = maestraSerializer(self.get_queryset(), many=True)
        return Response(MaestraData.data, status=status.HTTP_200_OK)

class MaestraViewDependencia(ListAPIView):
    queryset = TblMaestra.objects.all()
    serializer_class = maestraSerializer

    def get_queryset(self):
        return TblMaestra.objects.filter(maes_dependencia=self.request.data['dependencia'])

    def post(self, request, *args, **kwargs):
        MaestraData = maestraSerializer(self.get_queryset(), many=True)
        return Response(MaestraData.data, status=status.HTTP_200_OK)

class MaestraCreate(CreateAPIView):
    queryset = TblMaestra.objects.all()
    serializer_class = maestraSerializer

    def post(self, request, *args, **kwargs):
        createData = maestraSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class MaestraUpdate(UpdateAPIView):
    queryset = TblMaestra.objects.all()
    serializer_class = maestraSerializer

class MaestraDelete(DestroyAPIView):
    queryset = TblMaestra.objects.all()
    serializer_class = maestraSerializer