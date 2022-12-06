from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from  django.db.models.signals import post_save 
from django.dispatch import receiver
import sys
sys.setrecursionlimit(1500)

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class Answer(models.Model):
    answer_text = models.CharField(max_length=900)
    is_correct = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.answer_text

    class Meta:
        # ordering = ['-created_at']
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        indexes = [
            models.Index(fields=['answer_text'])
        ]

class Question(models.Model):
    question_text = models.CharField(max_length=900)
    answers = models.ManyToManyField(Answer)
    points = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='question')
    
    def __str__(self) -> str:
        return self.question_text

    class Meta:
        # ordering = ['-created_at']
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        indexes = [
            models.Index(fields=['question_text'])]

class Quizzes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    due = models.DateField()
    allowed_attempts = models.PositiveIntegerField()
    time_limit_mins = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    questions = models.ManyToManyField(Question,blank=True)

    def __str__(self) -> str:
        return self.title

class Attempter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    complited = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username


class Attempt(models.Model):
    quiz = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    attempter = models.ForeignKey(Attempter, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.attempter.user.username + ' - ' + self.answer.answer_text

@receiver(post_save, sender=Quizzes)
def update_lesson_banned(sender, instance, created, **kwargs):
    if created:
        questions = instance.category.question.all()
        for question in questions:
            instance.questions.add(question)
        instance.save()
