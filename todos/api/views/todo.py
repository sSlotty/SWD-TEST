from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Todo

class TodoList(APIView):
    
    def get(self, request):
        
        todo = Todo.objects.all()
        if len(todo) == 0:
            return Response({"error": "No data found"}, status=status.HTTP_400_BAD_REQUEST)
        
        data = {"todo": list(todo.values("title", "description"))}
        return Response(data)
    
    def post(self, request):
        title = request.data.get("title")
        description = request.data.get("description")
        
        if len(title) <= 0 or len(description) <= 0:
            return Response({"error": "Please provide both title and description"}, status=status.HTTP_400_BAD_REQUEST)
        
        exitTitle = Todo.objects.filter(title=title).values()
        if len(exitTitle) > 0:
            return Response({"error": "Title already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        
        todo = Todo.objects.create(title=request.data["title"], description=request.data["description"])
        data = {"todo": {"title": todo.title, "description": todo.description}}
        return Response(data, status=status.HTTP_201_CREATED)
    
    

class GetTodoListByID(APIView):
    
    def get(self, request, id):
        
        todo = Todo.objects.filter(title=id)
            
        if not todo.exists():
            return Response({"error": "No data found"}, status=status.HTTP_400_BAD_REQUEST)
        
        for i in todo.values():
            data = {"todo": {"title": i['title'], "description": i['description']}}
            
        # data = {"todo": {"title": todo.title, "description": todo.description}}
        return Response(data)

    def delete(self, request, id):
        todo = Todo.objects.filter(title=id)
        
        if not todo.exists():
            return Response({"error": "No data found"}, status=status.HTTP_400_BAD_REQUEST)
        todo.delete()
        
        return Response({"success": "Todo deleted successfully"}, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        todo = Todo.objects.filter(title=id)
        new_title = request.data.get("title")
        description = request.data.get("description")
        
        filter = Todo.objects.filter(title=new_title)
        if not todo.exists():
            return Response({"error": "No data found"}, status=status.HTTP_400_BAD_REQUEST)
        
        if len(filter) > 0:
            return Response({"error": "The newly entered name already exists in the database."}, status=status.HTTP_400_BAD_REQUEST)
        
        
        todo.update(title=new_title, description=description)
        
        return Response({"success": "Todo updated successfully"}, status=status.HTTP_200_OK)
    
    
