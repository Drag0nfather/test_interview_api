from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .models import Interview, Question
from .permissions import IsAdminOrReadOnly
from .serializers import InterviewSerializer, QuestionSerializer


class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    permission_classes = [IsAdminOrReadOnly]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        interview = get_object_or_404(Interview, id=self.kwargs['id'])
        return interview.questions.all()

    def perform_create(self, serializer):
        interview = get_object_or_404(Interview, pk=self.kwargs['id'])
        serializer.save(interview=interview)
