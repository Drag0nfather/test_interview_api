from django.contrib import admin
from api.models import Question, Interview, Answer


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question)
admin.site.register(Interview)
admin.site.register(Answer)
