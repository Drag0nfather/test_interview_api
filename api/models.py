from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Interview(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name


class TypeQuestion(models.TextChoices):
    TEXT = 'Ответ текстом'
    SINGLE_CHOICE = 'Выбор одного варианта'
    MULTIPLE_CHOICE = 'Выбор нескольких вариантов'


class Question(models.Model):
    text = models.CharField(max_length=300)
    type = models.CharField(max_length=50, choices=TypeQuestion.choices)
    interview = models.ForeignKey(Interview,
                                  blank=True,
                                  on_delete=models.CASCADE,
                                  related_name='questions')

    def __str__(self):
        return self.text


class Answer(models.Model):
    user_id = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='question')
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE, related_name='interview', blank=True, null=True)
    answer_data = models.CharField(max_length=300)

    def __str__(self):
        return self.answer_data
