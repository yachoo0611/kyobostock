from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('blog/', views.blog, name='blog'),
    path('new/', views.new, name='new'),
    path('blog/<int:blog_id>/', views.detail, name='detail'),
    path('blog/create/', views.create, name='create'),
    path('blog/delete/<int:blog_id>/', views.delete, name='delete'),
    path('blog/update/<int:blog_id>/', views.update, name='update'),
    path('blog/edit/<int:blog_id>/', views.edit, name='edit'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)