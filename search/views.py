# import sys
# sys.path.insert(0,r'C:\Users\smddu\Documents\GitHub\my-first-blog\search')
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

# def crawler(request, t):
#     soup = engine.search_engine(t)
#     #잘못된 입력(soup)이 들어온 경우, 다시 검색
#     if soup is False:
#         return render(request,'search/nobook.html')
#     b_info = engine.book_info(soup)
#     b_url = engine.book_url(soup)
#     # 작가, 출판사 존재유무 판단
#     try :
#         auth_toBe = Author.objects.get(name = b_info['auth'])
#     except:
#         auth_query = Author(name = b_info['auth'])
#         auth_query.save()
#     try :
#         pub_toBe = Publisher.objects.get(company = b_info['pub'])
#     except:
#         pub_query = Publisher(company = b_info['pub'])
#         pub_query.save()
#     # 작가, 출판사 object를 가져와 book 테이블에 입력
#     au = Author.objects.filter(name=b_info['auth'])[0]
#     pu = Publisher.objects.filter(company=b_info['pub'])[0]
#     book_query = Book(isbn = b_info['isbn'], title = b_info['title'], auth = au, pub = pu, image = b_info['img'], time = 0)
#     book_query.save()
#     # URL 입력
#     bo = Book.objects.filter(isbn = b_info['isbn'])
#     url_query = Url(book = bo[0], kb = b_url[0], yp = b_url[1], bd = b_url[2])
#     url_query.save()
#     isbn = bo[0].isbn
#     return HttpResponseRedirect(reverse('search:result', args=(isbn,)))

def result(request, isbn):
    stock = api_engine.getStock(str(isbn))
    context = {'stock': stock}
    return render(request, 'search/result.html', context)

# def maptest(request):
#     return render(request, 'search/maptest.html')