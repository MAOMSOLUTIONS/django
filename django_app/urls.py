# pet_api/urls.py

from django.urls import include, path
from rest_framework import routers
from pets.views import UserViewSet, PetViewSet,CustomTokenObtainPairView, CustomTokenRefreshView



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'pets', PetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),

]
