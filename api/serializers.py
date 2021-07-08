from rest_framework import serializers

from api.models import Interview


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'start_date', 'end_date', 'description')
        model = Interview
