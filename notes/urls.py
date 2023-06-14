from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view(), name="notes.list"),
    #this will make the path a specific note with its pk (an int) as part of it 
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name="notes.detail"),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name="notes.update"),
    path('notes/new', views.NotesCreateView.as_view(), name="notes.new"),
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name="notes.delete"),
]

