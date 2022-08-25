from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views
from .views import (OrderViewSet,
                    BlacklistTokenUpdateView,
                    CustomerTrailerViewSet,
                    CustomerViewSet, 
                    VehicleViewSet, 
                    DriverViewSet,
                    CustomerDriverViewSet, 
                    LoginView,
                    CustomerTruckViewSet,
                    BulkOrderViewSet)

router = DefaultRouter()
router.register('order', OrderViewSet, basename='customer order')
router.register('customer', CustomerViewSet, basename='customer')
router.register('vehicle', VehicleViewSet, basename='vehicle')
router.register('driver', DriverViewSet, basename='driver')
router.register('customer-driver', CustomerDriverViewSet, basename='customer-driver')
router.register('customer-truck', CustomerTruckViewSet, basename='customer-truck')
router.register('customer-trailer', CustomerTrailerViewSet, basename='customer-trailer')
router.register('bulk-order', BulkOrderViewSet, basename='bulk-order')

urlpatterns = [
    # path('', include(router.urls)),
    path("login/", LoginView.as_view(), name="login"),
    
    # path("order/", views.get_orders, name="get_orders"),
    # path('customer-trailer/', views.CustomerTrailerListView.as_view(), name='customer-trailer')

]

urlpatterns += router.urls