from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sets import views

# router = DefaultRouter()
# router.register('', views.SetsViewSet)
# app_name = 'set-cards'

# urlpatterns = [
#     path('sets/', include(router.urls)),
#     path('cards/<str:set_id>/', views.CardsViewSet.as_view(), name='cards'),
# ]



urlpatterns = [
    # GET /sets - List all sets
    path('sets/', views.SetsAllView.as_view(), name='sets-list'),
    
    # GET /sets/:id/cards - List all cards in a specific set
    path('sets/<str:id>/cards/', views.SetsCardsView.as_view(), name='set-cards'),
    
    # GET /cards/:id - Get detailed card information (Optional)
    path('cards/<str:id>/', views.CardsViewSet.as_view(), name='card-detail'),
]