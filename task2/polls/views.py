from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import redirect
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

from .models import Question

class AnswerView(CreateView):

    model = Answer
    form_class = AnswerForm

    def get(self, request):
        return redirect('polls/')

class AskView(CreateView):

    model = Question
    form_class = QuestionForm
    template_name = 'polls/ask.html'

    

class QuestionView(DetailView):

    model = Question
    template_name = 'polls/question.html'

    def get_form(self):
        return AnswerForm(initial={'question': self.kwargs['pk']})

class index(ListView):
    model = Question
    template_name = 'polls/index.html'
    def get_queryset(self):
        return Question.objects.order_by('-id')
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)