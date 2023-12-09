from django.urls import path, re_path
from apps.provas import views
from .views import question_list, answer_question, exam_detail, check_answers

urlpatterns = [

    # The home page
    path('provas/', views.provas, name='provas'),
    path('question/', question_list, name='question_list'),
    path('answer/<int:question_id>/', answer_question, name='answer_question'),
    path('provas/exam/<int:provas_id>/', exam_detail, name='exam_detail'),
    path('provas/exam/check_answers/<int:provas_id>/', check_answers, name='check_answers'),
    

]