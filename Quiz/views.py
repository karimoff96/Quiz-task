from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from Quiz.forms import NewQuestionForm, NewQuizForm
from Quiz.models import Answer, Question, Quizzes, Attempt, Attempter


def quizes(request):
    quizes = Quizzes.objects.all()
    return render(request, 'quiz/quiz.html', {'quizes': quizes})
