from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter


class TaskViewSet(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes=[IsAuthenticated] 
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_fields = ['completed']
    search_fields = ['title']
    ordering_fields = ['title', 'id']

#@api_view(['GET','POST'])
#def get_tasks(request):
    #if request.method == "GET":
        #tasks = Task.objects.all()
       # serializer = TaskSerializer(tasks, many=True)
       ## return Response(serializer.data)
   # elif request.method == "POST":
        #serializer=TaskSerializer(data=request.data)
        #if serializer.is_valid():
           # serializer.save()
           # return Response(serializer.data,status=status.HTTP_201_CREATED)
       # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#@api_view(['PUT'])
#def update_task(request,pk):
    #task=Task.objects.get(id=pk)
   # serializer=TaskSerializer(task,data=request.data)
    #if serializer.is_valid():
       # serializer.save()
       # return Response(serializer.data)
   # return Response(serializer.errors)

#@api_view(['DELETE'])
#def delete_task(request,pk):
   # task=Task.objects.get(id=pk)
    #task.delete()
   # return Response("Task deleted successfully")