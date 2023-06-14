from rest_framework import serializers
from apps.servicios.models import *
from apps.personas.models import *
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate
from django.db.models import CharField
from rest_framework.serializers import ModelSerializer, CharField, ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class DisponibilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponibilidad
        fields =('__all__')

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields=('__all__')

class maestraSerializer(ModelSerializer):
    class Meta:
        model = TblMaestra
        fields = '__all__'

class alquilerSerializer(ModelSerializer):
    inmueble_inmu_id = serializers.StringRelatedField()
    class Meta:
        model = TblAlquiler
        fields = '__all__'

class inmuebleSerializer(ModelSerializer):
    #tipo_inmueble = maestraSerializer(read_only=True)
    #tipo_estado = serializers.StringRelatedField()
    #dueño = serializers.StringRelatedField()
    class Meta:
        model = TblInmueble
        fields = '__all__'

class inmuebleDetailSerializer(ModelSerializer):
    pais_id = maestraSerializer(read_only=True)

    class Meta:
        model = TblInmueble
        fields = '__all__'

class pagoSerializer(ModelSerializer):
    class Meta:
        model = TblPago
        fields = '__all__'

class personaSerializer(ModelSerializer):
    #tipo_sexo = serializers.StringRelatedField()
    #tipo_identificacion = serializers.StringRelatedField()
    
    class Meta:
        model = TblPersona
        fields = ('__all__')

class usuarioSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])
        return user

class LoginSerializers(ModelSerializer):
    username = CharField()
    password = CharField()

    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        return ValidationError('Incorrect Credentials Passed.')