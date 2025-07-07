from django.urls import path
from . import views
from .views import NoteDeleteView

app_name = 'notes'

urlpatterns = [
    path('', views.home, name='home'),
    path('create_note/<int:subject_id>/', views.create_note, name='create_note'),
    path('subject/<int:subject_id>/', views.subject_detail, name='subject_detail'),
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
    path('note/<int:pk>/edit/', views.edit_note, name='edit_note'),
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='delete_note'),
]
