from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sets import views


urlpatterns = [
    path('sets/', views.SetsAllView.as_view(), name='sets-list'),
    path('sets/<str:id>/cards/', views.SetsCardsView.as_view(), name='set-cards'),
    path('cards/<str:id>/', views.CardsViewSet.as_view(), name='card-detail'),
]