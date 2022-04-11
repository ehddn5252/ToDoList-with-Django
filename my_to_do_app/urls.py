from django.urls import path
from . import views

urlpatterns = [
    # path 로 매핑 시킬 때 name 으로 값을 찾아서 매핑시켜준다.
    path('',views.index, name='index'),
    path('createTodo/',views.createTodo),
    path('deleteTodo/', views.doneTodo,name='deleteTodo')
]