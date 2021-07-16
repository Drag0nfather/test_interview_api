from django.conf.urls import url
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import (InterviewViewSet,
                    QuestionViewSet,
                    ActiveInterviewViewSet,
                    AnswerViewSet,
                    UserAnswersViewSet)

router = DefaultRouter()

router.register('interviews', InterviewViewSet)
router.register('interviews/(?P<id>\d+)/questions', QuestionViewSet)
router.register('active_interviews', ActiveInterviewViewSet)


urlpatterns = [
    url(r'interviews/(?P<interview_id>\d+)/questions/(?P<question_id>\d+)/answers',
        AnswerViewSet.as_view({'post': 'create_answer'})),

    url(r'interviews/(?P<interview_id>\d+)/answers/(?P<user_id>\d+)',
        UserAnswersViewSet.as_view({'get': 'get_passed_interviews'})),

    path('', include(router.urls)),
    path('token/', views.obtain_auth_token),
]
