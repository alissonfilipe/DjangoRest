from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json


#=============CHAMNDO TODOS OS VALORES - GET ======

#  1 - TODOS OS VALORES
@api_view(['GET'])

def get_users(request):

    if request.method == 'GET':
        users = User.objects.all() # buscando da tabela user
        serializer = UserSerializer(users, many=True) # conveter json todos, 
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# 2 - CHAMANDO PELA CHAVE PRIMARIA
@api_view(['GET'])
def get_by_nick(request, nick): #nick variavel passada na url

    try:
        usuario= User.objects.get(pk=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
#transformando o user em json
    
    if request.method =='GET': 

        serializer = UserSerializer(usuario)
        return Response(serializer.data)

#====================CRIANDO UM CRUD COMPLETO ====================
# 3 - CRUD
    
@api_view(['GET','POST','PUT','DELETE'])
def user_manager(request):

#ACESSO - GET
    
    if request.method == 'GET': 

        try:
            if request.GET['user']: #verifica o parametro da url /?user=xxxxxxx

                user_nickname = request.GET['user'] #encontrou o parametro get
                
                # BLOCO TRY => VALIDANDO SE O USUARIO FOI ENCONTRADO
                try:
                    user = User.objects.get(pk=user_nickname) #busca o objet no banco
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = UserSerializer(user) #serializa o objeto banco
                return Response(serializer.data) #retorno o json do objeto
            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

#CREAÇÃO - CREATE



    
   

    








# IMPORTANTE
# COMO SER COMPORTA O BANCO NO DJANCO
#     data = User.objects.get(pk='chave do banco')    #OBJETO
#     data = User.objects.first(user_age='25')        #QUERYSET - so que for 25
#     data = User.objects.exclude(user_age='25')      #QUERYSET - não for 25
#     data.save()
#     data.delete()
#      OBJECTS = []
#      
#      for objects in data:
#       objects.appened() -> adicionando
#       len(objects) -> tamanho do array
#