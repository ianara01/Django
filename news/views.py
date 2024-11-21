from django.shortcuts import render
from django.http import HttpResponse
from .models import Company, News

def index(request):
    companies = Company.objects.all()
    context = {'company_list': companies}
    return render(request, 'news/index.html', context)

def detail(request, company_id):
    companies = Company.objects.get(pk=company_id)
    context = {'company': companies}
    return render(request, 'news/detail.html', context)