"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import search.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('search.urls')),
    path('', include('accounts.urls')),
    path('', search.views.index, name='index'),
    path('', include('blogapp.urls')),

    # path('result/<int:isbn>/', search.views.result, name='result'),
    # path('select/', search.views.select, name='select'),
    # path('signup/', accounts.views.signup, name='signup'),
    # path('login/', accounts.views.login, name='login'),
    # path('logout/', accounts.views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
