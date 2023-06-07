# pet_api/urls.py

from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from pets.views import UserListCreateView, UserRetrieveUpdateDestroyView, PetListCreateView, PetRetrieveUpdateDestroyView, UserPetsListView, PetUserAssociationView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView 
)


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
    path('pets/', PetListCreateView.as_view(), name='pet-list-create'),
    path('pets/<int:pk>/', PetRetrieveUpdateDestroyView.as_view(), name='pet-retrieve-update-destroy'),
    path('users/<int:user_id>/pets/', UserPetsListView.as_view(), name='user-pets-list'),
    path('pets/<int:pk>/associate/', PetUserAssociationView.as_view(), name='pet-associate'),
]