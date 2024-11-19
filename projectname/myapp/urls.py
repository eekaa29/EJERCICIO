from django.urls import path
from .views import TaskListCreateView, TaskDetailView, AllTasksListView, TaskDeleteView, TaskUpdateView, UserListCreateView, UserDetailView, AllUsersListView, UserDeleteView, UserUpdateView 

urlpatterns = [path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
               path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
               path('tasks/all/', AllTasksListView.as_view(), name='all-tasks-list'),
               path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
               path('tasks/update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
               
               path('users/', UserListCreateView.as_view(), name='user-list-create'),
               path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
               path('users/all/', AllUsersListView.as_view(), name='all-users-list'),
               path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
               path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
               ]