from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Paciente
from .serializers import PacienteSerializer

import json

@api_view(['GET', 'POST','PUT','DELETE'])
def pacientes_crud(request):
    if request.method == 'GET':
        pacientes = Paciente.objects.all()

        serializer = PacienteSerializer(pacientes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        novo_paciente = request.data
        serializer = PacienteSerializer(data=novo_paciente)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def pacientes_by_id(request, id):
    if request.method == 'GET':
          paciente = Paciente.objects.get(pk=id)
          serializer = PacienteSerializer(paciente)
          return Response(serializer.data)
    
    if request.method == 'PUT':
        paciente_atualizar = Paciente.objects.get(pk=id)
        serializer = PacienteSerializer(paciente_atualizar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    if request.method == 'DELETE':
        paciente_deletar = Paciente.objects.get(pk=id)
        paciente_deletar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
