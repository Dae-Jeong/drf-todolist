from django.urls import path

from .views import (TodosAPIView, TodoAPIView,
                    DoneTodosAPIView, DoneTodoAPIView,
                    TodosMixinAPIView, TodoMixinAPIView,
                    DoneTodosMixinAPIView, DoneTodoMixinAPIView)

urlpatterns = [
    path('todo/', TodosAPIView.as_view()),
    path('todo/<int:pk>', TodoAPIView.as_view()),
    path('done/', DoneTodosAPIView.as_view()),
    path('done/<int:pk>', DoneTodoAPIView.as_view()),
    path('m-todo/', TodosMixinAPIView.as_view()),
    path('m-todo/<int:pk>', TodoMixinAPIView.as_view()),
    path('m-done/', DoneTodosMixinAPIView.as_view()),
    path('m-done/<int:pk>', DoneTodoMixinAPIView.as_view()),
]
