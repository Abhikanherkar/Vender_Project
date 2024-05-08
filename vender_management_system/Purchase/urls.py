from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Purchase.API.viewset import PrchaseViewset, PurchseStatusLog

# Create a router and register our ViewSets with it.
router = DefaultRouter()

router.register(r'purchase_orders', PrchaseViewset, basename='test')
router.register(r'purchase_status_log', PurchseStatusLog, basename='status_log  ')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    
]