from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment
from django.utils import timezone
from django.core.paginator import Paginator


# Create your views here.
def blog(request):
    blogs = Blog.objects
    blog_all = Blog.objects.all()
    paginator = Paginator(blog_all, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):

    details = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        Comment.objects.create(
            blog=details,
            comment_author=request.POST.get('comment_author'),
            comment_contents=request.POST.get('comment_contents'),
        )
        return redirect('/blog/' + str(details.id))

    return render(request, 'detail.html', {'details': details})

def new(request):
    if request.user.is_authenticated:
        # 로그인 한 상태라면 new포스트 html로 보내기.
        return render(request, 'new.html')
    else:
        # 회원정보가 존재하지 않는다면, 에러인자와 함께 home 템플릿으로 돌아가기.
        blogs = Blog.objects
        return render(request, 'blog.html', {'blogs': blogs, 'error': 'You have to login to make newpost'})
    return render(request, 'new.html')

def create(request):

    blog = Blog()
    blog.author = request.user
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.image = request.FILES['image']
    blog.pub_date = timezone.datetime.now()
    blog.save()

    return redirect('/blog/' + str(blog.id))

def delete(request, blog_id):
    destroy = get_object_or_404(Blog, pk=blog_id)
    destroy.delete()
    return redirect('blog')

def update(request, blog_id):
    updates = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'update.html', {'updates': updates})

def edit(request, blog_id):

    edit = Blog.objects.get(pk=blog_id)
    edit.title = request.POST['title']
    edit.body = request.POST['body']
    request.FILES['image'].delete()
    edit.image = request.FILES['image']
    edit.pub_date = timezone.datetime.now()
    edit.save()

    return redirect('blog')


def booksearch(request):
    blogs = Blog.objects.all().order_by('-id')

    q = request.POST.get('q', "")

    if q:
        blogs = blogs.filter(title__icontains=q)
        return render(request, 'booksearch.html', {'blogs': blogs, 'q': q})

    else:
        return render(request, 'booksearch.html')



