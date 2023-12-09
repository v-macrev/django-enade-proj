from django.db import models

class Provas(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='provas/images/')
    category = models.CharField(max_length=255)

class Question(models.Model):
    provas = models.ForeignKey(Provas, on_delete=models.CASCADE, default=1)
    text = models.CharField(max_length=255)

class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField('Correct answer', default=False)
