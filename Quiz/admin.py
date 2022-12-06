from django.contrib import admin
from Quiz.models import Quizzes, Question, Answer, Attempt, Attempter, Category
# Register your models here.

# class DictionaryWordAdmin(admin.ModelAdmin):
#     list_display = ['title', 'created_at', 'id']
#     search_fields = ['title']
#     show_full_result_count = True

admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Quizzes)
admin.site.register(Answer)
admin.site.register(Attempt)
admin.site.register(Attempter)
