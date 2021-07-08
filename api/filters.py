from datetime import datetime

from api.models import Interview


def actual_interviews():
    return Interview.objects.filter(end_date__gte=datetime.today())
