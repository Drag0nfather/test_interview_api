from typing import Dict

from rest_framework import serializers

from api.models import Interview, Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    interview = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'text', 'type', 'interview')
        model = Question


class InterviewSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(read_only=True, many=True)

    class Meta:
        fields = ('id', 'name', 'start_date', 'end_date', 'description', 'questions')
        model = Interview


class AnswerSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    interview_id = serializers.IntegerField()
    question_id = serializers.IntegerField()
    answer_data = serializers.CharField()

    def create(self, data: Dict):
        return Answer.objects.create(**data)


class UserAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('question_id', 'answer_data')
        model = Answer
