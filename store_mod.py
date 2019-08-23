# coding=utf-8
import requests
from django.db import models
from django.conf import settings
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from search.models import Store


if __name__ == "__main__":
    a = Store.objects.all()
    n = 0
    for i in a:
        n += 1
        s = str(i).replace('교보문고 ', '')
        q = Store.objects.filter(pk=(n)).update(place_name=s)
