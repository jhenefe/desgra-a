from pydoc import ModuleScanner
from types import CellType
from email.policy import default
from django.contrib.auth.models import User
from rest_framework import serializers
from django.db import models
from unittest.util import _MAX_LENGTH
from tasks.models import PadariaModel,ClienteModel,PadariaFavModel,FornadaPlanModel,FornadaAtModel

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email','password']

class PadariaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PadariaModel
        fields = ['id','nome','Cep', 'cnpj','email','statusFinanceiro','descricao','endereço','latitude','longitude']
class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClienteModel
        fields = ['idC','nome','Cep','email','telefone']

class PadariaFavSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PadariaFavModel
        fields = ['idPadaria','idCliente']

class FornadaPlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FornadaPlanModel
        fields = ['idPad','horario','url']


class FornadaAtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FornadaAtModel
        fields = ['idPada','horario','status','url']
