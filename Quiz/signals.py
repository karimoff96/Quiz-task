@receiver(post_save, sender=Quizzes)
def update_lesson_banned(sender, instance, created, **kwargs):

    questions = instance.category.question.all()
    for question in questions:
        instance.questions.add(question)
    instance.save()