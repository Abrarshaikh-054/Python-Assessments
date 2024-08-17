from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializers

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List' : '/task-list/',
        'Detail' : '/task-detail/<str:pk>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializers(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def task_detail(request,pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({'error':'Task not found'},status=404)
    
    serializer = TaskSerializers(task,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['PUT','PATCH'])
def task_update(request,pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({'error':'Task not found'},status=404)
    
    serializer = TaskSerializers(instance=task,data=request.data,partial=True if request.method == "PATCH" else False)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=400)

@api_view(['DELETE'])
def task_delete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Task deleted successfully..!!")