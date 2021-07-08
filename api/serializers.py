from rest_framework import serializers

from api.models import Interview, Question


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'start_date', 'end_date', 'description')
        model = Interview


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'text', 'type', 'interview')
        model = Question
