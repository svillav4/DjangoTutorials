from django.urls import path 
from . import views

urlpatterns = [ 
    path('todos/', views.ToDoListCreate.as_view(), name='list'), 
    path('todos/<int:pk>/', views.ToDoRetrieveUpdateDestroy.as_view(), name='todo_RUD'),
    path('todos/<int:pk>/complete/', views.ToDoToggleComplete.as_view()), 
    path('signup/', views.signup, name='signup'), 
    path('login/', views.login, name='login'), 
]
