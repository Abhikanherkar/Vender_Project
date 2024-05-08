from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Vender.API.viewset import VenderCreateViewset

# Create a router and register our ViewSets with it.
router = DefaultRouter()

router.register(r'venders', VenderCreateViewset, basename='test')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    
]