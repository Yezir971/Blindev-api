from django.urls import path, include
from .views import *
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('question', views.QuestionViewSet)
router.register('quizz', views.QuizzViewSet)
router.register('answer', views.AnswerViewSet)
router.register('result', views.ResultViewSet)
urlpatterns = [
    path('', include(router.urls)),
    
]