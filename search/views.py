from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
import api_engine

def index(request):
    return render(request,'search/index.html')

def select(request):
    t = request.POST.get('title')
    book = api_engine.bookInfo(t)
    context = {'b': book}
    return render(request, 'search/select.html', context)

def result(request, isbn):
    i = str(isbn)
    stock = api_engine.getStock(i)
    context = {'stock': stock}
    return render(request, 'search/result.html', context)