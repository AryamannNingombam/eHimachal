
from django.urls import path
from . import views
urlpatterns = [
    path('',views.apiOverview,name="apiOverview"),
    path('task-list/',views.taskList,name="taskList"),
    path('task-detail/<str:sno>/',views.taskDetailView,name="taskDetail"),
    path('task-create/',views.postNewTask,name='taskCreate'),
    path('task-update/<str:sno>',views.updateTask,name='taskUpdate')


]