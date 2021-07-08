from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import InterviewViewSet, QuestionViewSet, ActiveInterviewViewSet

router = DefaultRouter()

router.register('interviews', InterviewViewSet)
router.register('interviews/(?P<id>\d+)/questions', QuestionViewSet)
router.register('active_interviews', ActiveInterviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', views.obtain_auth_token),
]
