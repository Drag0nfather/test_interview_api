from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import InterviewViewSet

router = DefaultRouter()

router.register('reviews', InterviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', views.obtain_auth_token),
]
