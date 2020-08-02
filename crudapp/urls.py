from django.contrib import admin
from django.urls import path
from crudapp import views
urlpatterns = [
    path('', views.index, name='home'),
    path('delete/<int:id>/', views.delete_data, name='delete'),
    path('<int:id>/', views.update_data, name='update'),
]
