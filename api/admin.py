from django.contrib import admin
from api.models import Option, Question, Interview


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Option)
admin.site.register(Question)
admin.site.register(Interview)
