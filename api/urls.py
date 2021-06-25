from django.urls import path

from .views import TodoView, TodoEdit

urlpatterns = [
    path('todos/', TodoView.as_view()),
    path('todos/<str:pk>', TodoEdit.as_view()),
    ]