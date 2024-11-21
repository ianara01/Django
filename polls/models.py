from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200) # table id serial, name varchar(10)
    pub_date=models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >=timezone.now()-datetime.timedelta(days=1)
    def text_length(self):
        return len(self.question_text)

# polls에 model.py에 위 내용 입력
# config에 settings.py에 installed app에 'polls'항목 추가
# 터미널에서 python manage.py makemigrations 실행 -> polls에 migrations 디렉토리 파일이 생기는 것 확인
# python manage.py migrate 를 통해서 polls_questions 테이블 생성 확인

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.choice_text}_투표수:{self.votes}_질문:{self.question.question_text}"
    