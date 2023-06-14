from django.db import models
from django.conf import settings

class TblMaestra(models.Model):
    maes_nombre = models.CharField( db_column='MAES_NOMBRE', max_length=45, null=True, blank=True)
    maes_dependencia = models.CharField( db_column='MAES_DEPENDENCIA', max_length=45, null=True, blank=True)
    maes_valor = models.CharField( db_column='MAES_VALOR', max_length=45, null=True, blank=True)
    maes_estado = models.CharField( db_column='MAES_ESTADO', max_length=45, null=True, blank=True)

    def __str__(self) -> str:
        return '{}'.format( self.maes_nombre)
       

    class Meta:
        db_table = 'tbl_maestra'


class TblPersona(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    ciudad = models.CharField(max_length=45)
    num_identidad = models.CharField(max_length=45)
    tipo_sexo = models.ForeignKey(TblMaestra, blank=True, null=True, on_delete=models.SET_NULL, related_name='sexo')
    tipo_identificacion = models.ForeignKey(TblMaestra, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return '{}'.format( self.nombre)
        
    class Meta:
        db_table = 'tbl_persona'

class Cliente(models.Model):
    persona = models.ForeignKey(TblPersona, null=True, blank=True, on_delete=models.CASCADE)
    clie_nacionalidad = models.CharField(max_length=20)
    oficio = models.ForeignKey(TblMaestra, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.clie_nacionalidad

class TblDueñoHasInmueble(models.Model):
    tbl_dueño_id = models.ForeignKey(settings.AUTH_USER_MODEL,
        db_column='tbl_dueño_ID', max_length=45, on_delete=models.SET_NULL, blank=True, null=True)
    inmueble_inmu_id = models.ForeignKey(TblMaestra,
        db_column='Inmueble_INMU_ID', max_length=45, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'tbl_dueño_has_Inmueble'
      
    