from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationViewSet, UserAuthenticationViewSet

router = DefaultRouter()
router.register(r'register', UserRegistrationViewSet, basename='register')
router.register(r'authenticate', UserAuthenticationViewSet, basename='authenticate')

urlpatterns = router.urls
