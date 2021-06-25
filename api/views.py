from django.shortcuts import render

from rest_framework.views import APIView 
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerilaizer


class TodoView(APIView):
    def get(self, request, format=None):
        todos = Todo.objects.all()
        serializer = TodoSerilaizer(todos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data 
        serializer = TodoSerilaizer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    

class TodoEdit(APIView):
    def put(self, request, pk):
        data = request.data
        todo = Todo.objects.get(pk=pk)
        serializer = TodoSerilaizer(todo,data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        todo.delete()
        return Response({"Deleted"})
