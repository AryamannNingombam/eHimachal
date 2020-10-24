from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Task
from .Serializers import TaskSerializer
# Create your views here.
@api_view(['GET'])
def apiOverview(requests):
    api_urls = {
        'list':'/task-list/',
        'Detail View' : '/task-detail/<str:pk>',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str:pk>',
        'Delete' : '/task-delete/<str:pk>'
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(requests):
    tasks  = Task.objects.all()
    serializer = TaskSerializer(tasks,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetailView(requests,sno):
    task = Task.objects.get(sno = sno)
    serializer = TaskSerializer(task,many =False)
    return Response(serializer.data)

@api_view(['POST'])
def postNewTask(requests):
    serializer = TaskSerializer(data = requests.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateTask(requests,sno):
    task = Task.objects.get(sno = sno)

    serializer = TaskSerializer(instance = task,data = requests.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

