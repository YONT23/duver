from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
import json
from rest_framework.generics import ListAPIView
from rest_framework import status
import json as simplejson
from django.db.models import Count
from ..serializers import *
from rest_framework.response import Response
from ..servicios.models import *
from django.db.models.functions import Lower
from django.core.serializers.json import DjangoJSONEncoder


class Consulta1(APIView):

    def get(self, resquest, *args, **kwargs):
        clientes = TblPersona.objects.all().values()
        mujeres = TblPersona.objects.filter(tipo_sexo=3).values()
        hombres = TblPersona.objects.filter(tipo_sexo=2).values()

        response = {
            "clientes_totales": len(clientes),
            "clientes_mujeres": len(mujeres),
            "clientes_hombres": len(hombres)
        }

        return JsonResponse(response, safe=False)


class Consulta2(ListAPIView):
    queryset = TblAlquiler.objects.all().values(
        'fecha_inicio', 'precio', 'fecha_final')
    serializer_class = alquilerSerializer

    def get(self, resquest, *args, **kwargs):
        registros = alquilerSerializer(self.get_queryset(), many=True)
        return Response(registros.data, status=status.HTTP_200_OK)


class Consulta3(APIView):

    def get(self, resquest, *args, **kwargs):
        result_list = list(TblPago.objects.values('pago_fecha', 'pago_valor'))

        return HttpResponse(json.dumps(result_list))


class Consulta4(ListAPIView):
    queryset = TblPersona.objects.raw(
        'SELECT id, nombre, ciudad, correo FROM tbl_persona')
    serializer_class = personaSerializer

    def get(self, resquest, *args, **kwargs):
        registros = personaSerializer(self.get_queryset(), many=True)
        return Response(registros.data, status=status.HTTP_200_OK)


class Consulta5(ListAPIView):
    queryset = TblPersona.objects.exclude(ciudad='San Juan')
    serializer_class = personaSerializer

    def get(self, resquest, *args, **kwargs):
        registros = personaSerializer(self.get_queryset(), many=True)
        return Response(registros.data, status=status.HTTP_200_OK)


class Consulta6(ListAPIView):
    queryset = TblPersona.objects.order_by('nombre')
    serializer_class = personaSerializer

    def get(self, resquest, *args, **kwargs):
        registros = personaSerializer(self.get_queryset(), many=True)
        return Response(registros.data, status=status.HTTP_200_OK)

