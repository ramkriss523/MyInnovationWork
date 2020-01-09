from django.contrib import admin
from .models import UserData, QuestionData


# Register your models here.
# admin.site.register(UserData)

@admin.register(UserData)
class UserData(admin.ModelAdmin):
    list_display = ('fullname', 'signum', 'WhizzKid', 'Humanitarian', 'Reformer', 'Socialite', 'Sportsperson', 'Individualist')


# admin.site.register(QuestionData)

@admin.register(QuestionData)
class QuestionData(admin.ModelAdmin):
    list_display = ('question', 'option1', 'option2', 'option3', 'option4', 'option5', 'option6', 'image1'
                    , 'image2', 'image3', 'image4', 'image5', 'image6')
