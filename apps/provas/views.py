# provas/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Provas, Answers
from .forms import AnswerForm

def provas(request):
    provas_items = Provas.objects.all()
    context = {'provas_items': provas_items}
    return render(request, 'provas/provas.html', context)

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'provas/question_list.html', {'questions': questions})

def answer_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('question_list')
    else:
        form = AnswerForm()
    return render(request, 'provas/answer_question.html', {'form': form, 'question': question})

from django.shortcuts import render, get_object_or_404
from .models import Provas

def exam_detail(request, provas_id):
    provas = get_object_or_404(Provas, pk=provas_id)
    questions = provas.question_set.all()  # Retrieve all questions for the exam
    answers = Answers.objects.all()
    return render(request, 'provas/exam_detail.html', {'provas': provas, 'questions': questions, 'answers': answers })


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def check_answers(request, provas_id):
    provas = get_object_or_404(Provas, pk=provas_id)
    questions = provas.question_set.all()

    if request.method == 'POST':
        correct_answers = 0
        for question in questions:
            selected_answer_id = request.POST.get(f'question_{question.id}')
            if selected_answer_id:
                selected_answer = get_object_or_404(Answers, pk=selected_answer_id)
                if selected_answer.is_correct:
                    correct_answers += 1

        # You can now use the value of `correct_answers` to determine if all answers are correct,
        # and provide feedback accordingly.

        if correct_answers == len(questions):
            feedback = "Congratulations! All answers are correct."
        else:
            feedback = f"You got {correct_answers} out of {len(questions)} correct."

        return render(request, 'provas/feedback.html', {'feedback': feedback})

    return HttpResponse("Invalid request.")
