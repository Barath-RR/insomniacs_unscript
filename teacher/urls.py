from django.urls import path

from teacher.views import index, viewcourse
urlpatterns = [
    path('', index, name='index'),
    path('view', viewcourse , name='viewc'),
]
    