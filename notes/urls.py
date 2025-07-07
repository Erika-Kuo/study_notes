from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.home, name='home'),
    path('create_note/<int:subject_id>/', views.create_note, name='create_note'),
]
