from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .filters import get_actual_interviews
from .models import Interview, Question, Answer
from .permissions import IsAdminOrReadOnly
from .serializers import InterviewSerializer, QuestionSerializer, AnswerSerializer, UserAnswerSerializer


class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    permission_classes = [IsAdminOrReadOnly]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        interview = get_object_or_404(Interview, id=self.kwargs.get('id'))
        return interview.questions.all()

    def perform_create(self, serializer):
        interview = get_object_or_404(Interview, pk=self.kwargs.get('id'))
        serializer.save(interview=interview)


class ActiveInterviewViewSet(viewsets.ModelViewSet):
    queryset = get_actual_interviews()
    serializer_class = InterviewSerializer
    permission_classes = [AllowAny]


class AnswerViewSet(viewsets.ViewSet):

    def create_answer(self, request, interview_id: int, question_id: int) -> Response:
        answer = request.data
        answer['interview_id'] = interview_id
        answer['question_id'] = question_id
        if Answer.objects.filter(user_id=answer.get('user_id')):
            return Response(data={'success': 'false'}, status=400)
        serializer = AnswerSerializer(data=answer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={'success': 'yes'}, status=200)


class UserAnswersViewSet(viewsets.ViewSet):

    def get_passed_interviews(self, request, interview_id: int, user_id: int) -> Response:
        answer = Answer.objects.filter(user_id=user_id, interview_id=interview_id)
        serializer = UserAnswerSerializer(answer, many=True)
        return Response(serializer.data)
