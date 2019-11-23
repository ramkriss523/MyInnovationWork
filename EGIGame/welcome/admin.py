from django.contrib import admin
from .models import UserData,QuestionData

# Register your models here.
admin.site.register(UserData)
# admin.site.register(QuestionData)

@admin.register(QuestionData)
class QuestionData(admin.ModelAdmin):
    list_display = ('question','option1','option2','option3','option4','option5','option6')