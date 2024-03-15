from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('man_list/', views.man_list, name='man_list'),
    path('add_man/', views.add_man, name='add_man'),
    path('woman_list/', views.woman_list, name='woman_list'),
    path('add_woman/', views.add_woman, name='add_woman'),
]