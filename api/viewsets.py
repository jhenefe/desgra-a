from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from horadopao.api.serializers import UserSerializer,PadariaSerializer,ClienteSerializer,PadariaFavSerializer,FornadaPlanSerializer,FornadaAtSerializer
from tasks.models import PadariaModel,ClienteModel,PadariaFavModel,FornadaPlanModel,FornadaAtModel
from rest_framework.authtoken.views import obtain_auth_token
from datetime import datetime
from django.http import JsonResponse
import requests
import json

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer 

class PadariaViewSet(viewsets.ModelViewSet):
    queryset = PadariaModel.objects.all()
    serializer_class = PadariaSerializer

    def create(self, request):
        # Criar uma instância do modelo PadariaModel com campos preenchidos pelo Django
        usuario = PadariaModel(id=request.data['id'],nome=request.data['nome'], Cep=request.data['Cep'], cnpj=request.data['cnpj'], email=request.data['email'], statusFinanceiro=request.data['statusFinanceiro'], descricao=request.data['descricao'], endereço=request.data['endereço'])

        # Obter os dados da API externa e atualizar a instância do modelo com eles
        api_data = obter_dados_da_api_externa(request.data['endereço'])
        # Verificar se há dados na resposta da API antes de tentar carregá-los como JSON
        if api_data:
            try:      
                usuario.latitude = api_data[0]['lat']   
                usuario.longitude = api_data[0]['lon']
            except json.JSONDecodeError as e:
                # Tratar exceção se os dados da API não estiverem em formato JSON válido
                return Response({'error': 'Erro ao carregar os dados da API: ' + str(e)}, status='status.HTTP_400_BAD_REQUEST')

        # Salvar a instância do modelo PadariaModel
        usuario.save()

        # Serializar a instância do modelo PadariaModel e retornar a resposta
        serializer = self.get_serializer(usuario)
        return Response(serializer.data)

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = ClienteModel.objects.all()
    serializer_class = ClienteSerializer
     

class PadariaFavViewSet(viewsets.ModelViewSet):
    queryset = PadariaFavModel.objects.all()
    serializer_class = PadariaFavSerializer

class FornadaPlanViewSet(viewsets.ModelViewSet):
    queryset = FornadaPlanModel.objects.all()
    serializer_class = FornadaPlanSerializer

class FornadaAtViewSet(viewsets.ModelViewSet):
    queryset = FornadaAtModel.objects.all()
    serializer_class = FornadaAtSerializer




def obter_dados_da_api_externa(endereço):

    url = 'https://nominatim.openstreetmap.org/search?q='+endereço+'&limit=2&format=json' 
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
