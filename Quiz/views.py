from django.shortcuts import redirect,render
from .forms import addQuestionform
from .models import QuesModel

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    if request.method == 'POST':
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            answer = request.POST.get(q.question) # Gets user’s choice, i.e the key of answer
            if q.ans == answer:
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        # print(context)
        return render(request,'Quiz/result.html',context)
    else:
        if len(QuesModel.objects.all())> 0:
            questions=QuesModel.objects.all()
            context = {
                'questions':questions
            }
            return render(request,'Quiz/home.html',context)
        else:
            return redirect('addquestion')

            
@login_required
def addQuestion(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'Quiz/addquestion.html',context)
    else: 
        return redirect('home-page') 
 