from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_list, name='register_list'),
    path('show/all',views.show_list,name='show_list'),
    path('show/<int:pk>',views.show_individual,name='show_individual'),
    path('show',views.login,name='login'),
]