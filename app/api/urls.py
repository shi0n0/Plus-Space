from django.urls import path
from app.api import views

urlpatterns = [
    path('profile/', views.ListView.as_view, name="profileTop"),
    path('profile/<int:pk>/', views.DetailView.as_view, name="profileDetail"),
]