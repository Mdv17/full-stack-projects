from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage
from . import views


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView, name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    # We are writing views because import views here and dot the app name. We are giving our path name called task
    # Our urls resolver cant use class inside of it thats why we are using as.view
    path('', TaskList.as_view(), name='tasks'),
    # views by default looks for the primary key (pk) value. Here set at it as an integer setting that to pk(task/<int:pk>)
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
]