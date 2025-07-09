from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addT, name="addT"),
    path('done/<int:pk>/', views.done, name='done'),
    path('undo/<int:pk>/', views.undo, name='undo'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name="delete"),
]
