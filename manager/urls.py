from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('add/', views.addItem, name="add-item"),
    path('update/<int:pk>/', views.updateItem, name="update-item"),
    path('delete/<int:pk>/', views.deleteItem, name="delete-item")
]
