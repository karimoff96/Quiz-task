from django.urls import path
from Quiz.views import home, addQuestion
urlpatterns = [
    path('', home,name='home-page'),
    path('addQuestion/', addQuestion,name='addquestion'),
]