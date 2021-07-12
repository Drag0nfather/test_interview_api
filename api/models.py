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


class Option(models.Model):
    name = models.CharField(max_length=300)
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name='options')

    def __str__(self):
        return self.name


class Answer(models.Model):
    user_id = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='question')
    many_options = models.ManyToManyField(Option)
    one_option = models.ForeignKey(Option, null=True,
                                   on_delete=models.CASCADE,
                                   related_name="one_option")
    text = models.TextField(null=True)

    def __str__(self):
        return self.text
