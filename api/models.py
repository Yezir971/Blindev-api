from django.db import models

from django.contrib.auth.models import User


TOPIC_CHOICE = (
    ("JARGON MARKET", "JARGON MARKET"),
    ("EDITEURS / SOFTS / OUTILS", "EDITEURS / SOFTS / OUTILS"),
    ("LANGAGES / FRAMEWORKS / BIBLIOTHEQUES", "LANGAGES / FRAMEWORKS / BIBLIOTHEQUES"),
    ("BUISNESS MODEL", "BUISNESS MODEL"),
    ("METRICS", "METRICS")
)
class Quizz(models.Model):
    title = models.CharField(max_length=200)
    topic = models.CharField(choices=TOPIC_CHOICE)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Temps du quizz en minute")
    require_score_to_pass = models.IntegerField(help_text="nombre de points minimum")

    def __str__(self):
        return f"{self.title}-{self.topic}"
    def get_questions(self):
        return self.question_set.all()

# Create your models here.
class Questions(models.Model):
    terme = models.CharField(max_length=200)
    quizz = models.ForeignKey(Quizz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.terme)
    def get_answer(self):
        return self.answer_set.all()
    
class Answer(models.Model):
    terme = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Définition : {self.question.terme}, answer {self.terme}, correct {self.correct}"
    
    
    
    

class Result(models.Model):
    quiz = models.ForeignKey(Quizz, on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    score = models.FloatField()
    
    def __str__(self):
        return str(self.pk)