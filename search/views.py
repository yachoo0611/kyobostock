from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.core import serializers
from .models import Store
import api_engine


def index(request):
    return render(request, 'search/index.html')


def select(request):
    t = request.POST.get('title')
    book = api_engine.bookInfo(t)
    if not book:
        return render(request, 'search/nobook.html')
    context = {'b': book, 't': t}
    return render(request, 'search/select.html', context)


def result(request, isbn):
    # i = request.POST.get('isbn')
    i = str(isbn)
    stock = api_engine.getStock(i)
    n = 0
    for i in stock.values():
        n += 1
        i = int(i)
        q = Store.objects.filter(pk=n).update(stock=i)
    seoul = serializers.serialize('json', Store.objects.filter(in_seoul=True), ensure_ascii=False)
    not_seoul = serializers.serialize('json', Store.objects.filter(in_seoul=False), ensure_ascii=False)
    context = {'stock': stock, 'in_seoul': seoul, 'not_seoul': not_seoul}
    return render(request, 'search/result.html', context)
