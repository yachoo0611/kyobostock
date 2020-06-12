from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment
from django.utils import timezone

# Create your views here.
def blog(request):

    blogs = Blog.objects
    return render(request, 'blog.html', {'blogs': blogs})


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



