from django import views
from django.urls import path, include

# from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import (LoginView, 
                    ScanOrder, 
                    LabInspectionListCreateAPIView,
                    SafetyCheckListCreateAPIView, 
                    SafetyCheckListQuestionCreateAPIView, 
                    SafetyCheckListDetailAPIView)

# from accounts.views import UserCreate

# from .views import OrderViewSet, ScanOrderViewset



urlpatterns = [    
    
    # path('', include(**args, **kwargs).urls),
    path("login/", LoginView.as_view(), name="login"),
    path("scan-order/<int:pk>/", ScanOrder.as_view(), name="scan-order"),
    # path("users/", UserCreate.as_view(), name="user_create"),
    path('checklist/', SafetyCheckListCreateAPIView.as_view(), name="check-list"),
    path('checklist/<int:pk>/', SafetyCheckListDetailAPIView.as_view(), name="detail-checklist"),
    path('checklist-questions/', SafetyCheckListQuestionCreateAPIView.as_view(), name="checklistquestions"),
    path('lab-inspection/', LabInspectionListCreateAPIView.as_view(), name="lab-inspection"),
    # path('order-new/<int:pk>/',views.OrderUpdate.as_view()),
    # path('order-new/<int:pk>/',views.OrderUpdate.as_view()),
    
]