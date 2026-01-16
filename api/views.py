from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from .models import Quizz, Questions, Answer, Result
from .serializers import QuestionSerializer, QuizzSerializer, AnswerSerializer, ResultSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all().order_by('terme')
    serializer_class = QuestionSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['terme', 'quizz__title']
    ordering_fields = ['terme', 'created']
class QuizzViewSet(viewsets.ModelViewSet):
    queryset = Quizz.objects.all().order_by('title')
    serializer_class = QuizzSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'topic']
    ordering_fields = ['title', 'topic']
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('terme')
    serializer_class = AnswerSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['terme', 'question__terme']
    ordering_fields = ['terme', 'created']
class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all().order_by('pk')
    serializer_class = ResultSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['quiz__title', 'user__username']
    ordering_fields = ['score', 'pk']
