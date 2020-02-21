from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:word_id>', views.detail, name = 'detail'),
    path('delete/<int:word_id>', views.delete, name = 'delete'),
    path('new/', views.new, name = 'new'),
    path('create', views.create, name = 'create'),
    path('edit/<int:word_id>', views.edit, name = 'edit'),
    path('update/<int:word_id>', views.update, name = 'update'),
]