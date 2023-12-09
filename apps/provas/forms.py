from django import forms
from .models import Answers

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ['text']