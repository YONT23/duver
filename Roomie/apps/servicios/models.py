from unicodedata import name
from django.db import models
from django.conf import settings
from apps.personas.models import *

class Disponibilidad(models.Model):
    disp_disponible = models.CharField(max_length=2)
    disp_precio = models.BigIntegerField()

    def __str__(self):
        return self.disp_disponible

class TblInmueble(models.Model):
    ciudad = models.CharField(max_length=45)
    estrato = models.CharField(max_length=45)
    pais_id = models.ForeignKey(TblMaestra, on_delete=models.CASCADE, related_name='pais')
    longitud = models.CharField(max_length=45, blank=True, null=True)
    latitud = models.CharField(max_length=45, blank=True, null=True)
    num_pisos = models.IntegerField()
    num_baños = models.IntegerField()
    num_habitaciones = models.IntegerField()
    url_imagenes = models.CharField(max_length=1000)
    superficie = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    tipo_inmueble = models.ForeignKey(
        TblMaestra, blank=True, null=True, on_delete=models.SET_NULL, related_name='Tinmueble')
    tipo_estado = models.ForeignKey(
        TblMaestra, blank=True, null=True, on_delete=models.SET_NULL)
    dueño = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'tbl_Inmueble'

class TblAlquiler(models.Model):
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    precio = models.CharField(max_length=45)
    inmueble_inmu_id = models.ForeignKey(TblMaestra,
        db_column='Inmueble_INMU_ID', blank=True, null=True, max_length=45, on_delete=models.SET_NULL)
    usuario_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'tbl_alquiler'

class TblPago(models.Model):
    pago_fecha = models.DateField(db_column='PAGO_fecha', max_length=45)
    pago_valor = models.CharField(db_column='PAGO_valor', max_length=45)
    tbl_alquiler_alqu_id = models.ForeignKey(TblAlquiler,
        db_column='tbl_alquiler_ALQU_ID', blank=True, null=True, on_delete=models.SET_NULL)
    tipo_pago = models.ForeignKey(
        TblMaestra, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'tbl_pago'

