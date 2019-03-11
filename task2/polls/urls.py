from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index.as_view(), name='index'),
    # the 'name' value as called by the {% url %} template tag
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
    path('ask', views.AskView.as_view(), name='ask'),
    path('answer', views.AnswerView.as_view(), name='answer'),
    path('q<int:pk>', views.QuestionView.as_view(), name='question'),
]