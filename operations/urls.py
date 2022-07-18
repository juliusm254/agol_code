from django import views
from django.urls import path, include

from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import LoginView

from .views import OrderViewSet, SafetyViewSet, ChecklistViewSet


router = DefaultRouter()
router.register('order', OrderViewSet, basename='order')
router.register('safety', SafetyViewSet, basename='safety')
router.register('check-list', ChecklistViewSet, basename='check-list')



# checklist_list_view = ChecklistViewSet.as_view({
#     "get": "list",
#     "post": "create"
# })


urlpatterns = [    
    
    # path('', include(router.urls)),
    path("login/", LoginView.as_view(), name="login"),
    # path('checklist/<int:pk>/',views.checklist),
    # path('order-new/<int:pk>/',views.OrderUpdate.as_view()),
    
]

urlpatterns += router.urls