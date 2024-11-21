#from django.contrib import admin
from django.utils import timezone
from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
        # 루트 경로
    path("", views.index, name="index"),
    
    # 동적 URL 경로
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),

    # 정적 URL 경로
    path('recent/', views.recent_questions, name='recent_questions'),
    path('questions_today/', views.questions_today, name='questions_today'),
    path('hello/', views.hello_world, name='hello_world'),
    path('questions_this_year/', views.questions_this_year, name='questions_this_year'),

]


