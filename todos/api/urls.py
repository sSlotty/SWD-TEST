from django.urls import path
from api.views import todo
urlpatterns = [

    path('todo/', todo.TodoList.as_view(), name='todo_list'),
    path('todo/<str:id>/', todo.GetTodoListByID.as_view(), name='todo_list_by_id'),

]