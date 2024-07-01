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
    
# CRUD completo para usuários
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):
    if request.method == 'GET':
        # Consultar usuário por nick, se fornecido como query parameter
        try:
            user_nickname = request.GET.get('user')
            user = User.objects.get(user_nickname=user_nickname)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            user_nickname = request.data.get('user')
            user = User.objects.get(user_nickname=user_nickname)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            user_nickname = request.data.get('user')
            user = User.objects.get(user_nickname=user_nickname)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)