from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:person_id>/', views.delete_person, name='delete_person'),
]
