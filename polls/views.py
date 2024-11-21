from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question, Choice
from django.utils.timezone import now

# Create your views here.

# function based 
def index(request):  # structure to ask request
    questions = Question.objects.all()  # Question 테이블에서 모든 row를 가져오기
    #try:
    #    q_text = Question.objects.all()  # pk=1인 질문을 가져옴

    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")  # 질문이 없으면 404 에러 반환
    #return HttpResponse(f"<h1>Question <i>내용</i> {q_text}</h1>")
    context = {"questions": questions}              # 보내기 (data 주기)
    return render(request, 'polls/index.html', context=context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    } # 수정 완료
    return render(request, 'polls/detail.html', context=context)
'''
    try:
        question = Question.objects.get(pk=question_id)
        choice_list = question.choice.set.all()
        context = {
            'question': question,
            'choice_list': choice_list
            }
    except Question.DoesNotExist:
        raise Http404("Question does not exist")  # 질문이 없으면 404 에러 반환
'''
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        # POST 데이터를 가져오기
        lion = request.POST.get('lion', '')  # POST 요청에서 'lion' 값을 가져옵니다.
        tiger = request.POST.get('tiger', '')  # POST 요청에서 'tiger' 값을 가져옵니다.

        # 결과 응답
        return HttpResponse("You're voting on question %s. Lion: %s, Tiger: %s." % (question.question_text, lion, tiger))
    

    # GET 요청일 경우 투표 페이지 렌더링
    return render(request, 'polls/vote.html', {'question': question})
def recent_questions(request):
    
    # pub_date 기준으로 내림차순 정렬하여 가장 최근의 10개 질문 가져오기
    recent_questions = Question.objects.all().order_by('-pub_date')[:3]

    # 결과를 HttpResponse로 반환하거나 템플릿을 통해 반환할 수 있음
    question_list = "\n".join([q.question_text for q in recent_questions])
    return HttpResponse(f"최근 10개의 질문: \n{question_list}")

def questions_today(request):
    # 현재 날짜를 가져옵니다.
    today = now().date()
    
    # pub_date가 오늘 날짜인 Question 객체들 필터링
    questions_today = Question.objects.filter(pub_date__date=today)
    
    # 질문들의 텍스트를 쉼표로 구분된 문자열로 결합
    question_texts = ", ".join([q.question_text for q in questions_today])
    
    # 결과를 HttpResponse로 반환
    return HttpResponse(f"오늘의 질문들: {question_texts}")

def hello_world(request):
    return HttpResponse("Hello, world!")

def questions_this_year(request):
    # 현재 연도를 계산
    current_year = now().year
    
    # pub_date의 연도가 현재 연도인 Question 객체 필터링
    questions = Question.objects.filter(pub_date__year=current_year)[:3]
    
    # 질문들의 텍스트를 쉼표로 구분된 문자열로 반환
    question_texts = ", ".join([q.question_text for q in questions])
    
    # 결과를 HttpResponse로 반환
    return HttpResponse(f"올해의 질문들: {question_texts}")
