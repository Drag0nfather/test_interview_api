from rest_framework import serializers

from api.models import Interview, Question, Option, Answer


class QuestionSerializer(serializers.ModelSerializer):
    interview = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'text', 'type', 'interview')
        model = Question


class OptionSerializer(serializers.ModelSerializer):
    question = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'name', 'question')
        model = Option


class InterviewSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(read_only=True, many=True)

    class Meta:
        fields = ('id', 'name', 'start_date', 'end_date', 'description', 'questions')
        model = Interview


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('user_id', 'interview', 'question', 'option', 'choice_text')
        model = Answer
