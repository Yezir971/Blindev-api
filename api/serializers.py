
from rest_framework import serializers
from .models import Quizz, Questions, Answer, Result

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'terme', 'correct', 'question']
class QuestionSerializer(serializers.ModelSerializer):
    answer_set = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Questions
        fields = ['id', 'terme', 'quizz', 'created', 'answer_set']
class QuizzSerializer(serializers.ModelSerializer):
    question_set = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Quizz
        fields = ['id', 'title', 'topic', 'number_of_questions', 'time', 'require_score_to_pass', 'question_set']
class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['id', 'quiz', 'user', 'score']

