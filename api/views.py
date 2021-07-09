from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from .filters import actual_interviews
from .models import Interview, Question, Option
from .permissions import IsAdminOrReadOnly
from .serializers import InterviewSerializer, QuestionSerializer, OptionSerializer


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
    queryset = actual_interviews()
    serializer_class = InterviewSerializer
    permission_classes = [AllowAny]


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        question = get_object_or_404(Question,
                                     pk=self.kwargs.get('question_pk'),
                                     interview__id=self.kwargs.get('id'))
        serializer.save(question=question)

    def get_queryset(self):
        question = get_object_or_404(Question,
                                     id=self.kwargs.get('question_pk'))
        return question.options.all()
